from http.client import HTTPS_PORT
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Max, Count, F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import BidForm, ListingForm, CommentForm, BidForm
from .models import User, Listing, Comment, Bid, Favourites


########## login / logout / register ##########

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions_list", kwargs={ 'filter':'active', 'cat':'all' }))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse('auctions_list', kwargs={'filter':'active','cat':'all'}))
    else:
        return render(request, "auctions/register.html")



########## lists ###########

def index(request):
    auctions = Listing.objects.filter(active=True)\
                .annotate(comments = Count('comment', distinct=True)).annotate(bids= Count('bid', distinct=True)).annotate(max_offer=Max('bid__amount'))
    return render(request, "auctions/index.html", {
            'list': auctions,
            'title': 'These are our current auctions',
            'filter': 'active'
    }) 


@login_required
def auctions_list(request, filter, cat):
    match filter:
        case 'active':
            auctions = Listing.objects.filter(active=True)\
                .annotate(comments = Count('comment', distinct=True))\
                .annotate(bids= Count('bid', distinct=True))\
                .annotate(max_offer=Max('bid__amount'))
            title = 'Currently active auctions'
        case 'own':
            auctions = Listing.objects.filter(creator_user_id=request.user.id)\
                .annotate(comments=Count('comment', distinct=True)).annotate(bids=Count('bid', distinct=True))
            title = 'My created auctions'
        case 'favourite':
            auctions = Listing.objects.filter(favourites__user=request.user.id, favourites__favourite=True)\
                .annotate(max_date=Max('favourites__listing__favourites__date')).values()\
                .filter(favourites__date=F('max_date'), favourites__favourite=True)\
                .annotate(comments=Count('comment', distinct=True)).annotate(bids=Count('bid', distinct=True))
            title = 'My watchlist'
        case 'won':
            auctions = Listing.objects.filter(buyer_id=request.user.id)\
                .annotate(comments=Count('comment', distinct=True)).annotate(bids=Count('bid', distinct=True))
            title = 'Won auctions'
    if cat != 'all':
        auctions = auctions.filter(category=cat)
        category = [item for item in Listing._meta.get_field('category').choices if item[0] == cat][0][1]
    else:
        category = None

    return render(request, "auctions/auctions_list.html", {
            'list': auctions,
            'title': title,
            'filter': filter,
            'category_name': category
    })


########## actions ############


@login_required
def create_auction(request):
    if request.method == 'POST':
            listingForm = ListingForm(request.POST)
            if listingForm.is_valid():
                new_instance = listingForm.save(commit=False)
                new_instance.creator_user_id = request.user.id
                new_instance.save()
                return HttpResponseRedirect(reverse('auctions_list', kwargs={'filter':'active','cat':'all'}))
            return render(request, 'auctions/listing_form.html', {'listingForm': listingForm, 'message':'Invalid form data' })
    return render(request, 'auctions/listing_form.html',{'listingForm':ListingForm(), 'message': ''})


def show_auction(request, id):
    listing = Listing.objects.get(pk=id)
    comments = Comment.objects.filter(listing=id).order_by('-date')
    favs = Favourites.objects.filter(listing_id=id, user_id=request.user.id)
    fav = favs.order_by('-date')[0].favourite if favs.exists() else False
    bids = Bid.objects.filter(listing=id)
    bids_count = bids.aggregate(Count('id'))['id__count']
    max_bid = bids.order_by('-amount')[0].amount if bids.exists() else 0
    min_possible_bid = max_bid+1 if len(bids)>0 else listing.starting_bid +1
    if request.method == "POST":
        if request.POST.__contains__('description'):
            form = CommentForm(request.POST)
        if request.POST.__contains__('amount'):
            form = BidForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=request.user.id)
            listing = listing
            newInstance = form.save(commit=False)
            newInstance.listing = listing
            newInstance.user = user
            newInstance.save()
            return HttpResponseRedirect(reverse('show_auction', args=[id]))
        return HttpResponseRedirect(reverse('show_auction', args=[id]) )
    return render(request, "auctions/listing.html", {
        'listing': listing,
        'comment_form': CommentForm(),
        'bid_form': BidForm(),
        'comments': comments,
        'max_bid': max_bid,
        'min_possible_bid': min_possible_bid,
        'fav': fav,
        'bids_count': bids_count
    })


@login_required
def activate(request, listing):
     listing_to_update = Listing.objects.filter(id=listing)
     buyer = Bid.objects.filter(listing=listing).order_by('-amount')[0].user
     if listing_to_update[0].active:
            listing_to_update.update(active=False)
            listing_to_update.update(buyer=buyer)
     else:
            listing_to_update.update(active=True)
            listing_to_update.update(buyer=None)
     return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favourite(request, listing, user):
     favs = Favourites.objects.filter(listing_id=int(listing), user_id=int(user))
     if favs.exists():
        fav = favs.order_by('-date')[0].favourite
        if fav:
            Favourites.objects.create(listing_id=listing, user_id=user, favourite=False)
        else:
            Favourites.objects.create(listing_id=listing, user_id=user, favourite=True)
     else:
        Favourites.objects.create(listing_id=listing, user_id=user, favourite=True)
     return HttpResponseRedirect(request.META['HTTP_REFERER'])


