from django.db import models
from django.db.models import fields
from django.forms import ModelForm, forms
from .models import Listing, Comment, Bid



class ListingForm(ModelForm):
        class Meta:
            model = Listing
            fields = ['title', 'description', 'starting_bid', 'image_url', 'category' ]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount', 'note']
