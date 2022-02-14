from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Listing, Comment, Bid, Favourites

# Register your models here.



class CommentAdmin(admin.ModelAdmin):
    list_display = ('description', 'user', 'date', 'listing')

admin.site.register(Comment, CommentAdmin)


class BidAdmin(admin.ModelAdmin):
    list_display = ('listing', 'note', 'user', 'amount', 'date')

admin.site.register(Bid, BidAdmin)

admin.site.register(User, UserAdmin)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'starting_bid', 'image_url', 'creator_user', 'buyer', 'active')

admin.site.register(Listing, ListingAdmin)

class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('listing', 'user', 'favourite', 'date')

admin.site.register(Favourites, FavouriteAdmin)