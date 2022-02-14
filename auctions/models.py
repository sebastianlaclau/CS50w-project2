
from curses.ascii import NUL
from django.contrib.auth.models import AbstractUser
from django.db import models

   
class User(AbstractUser):
    pass

class Listing(models.Model):
    
    class Category(models.TextChoices):
        FA = 'FA', 'Fashion'
        CE = 'CE', 'Consumer Electronics'
        SG = 'SG', 'Sporting goods',
        HW =  'HW', 'Health & Wellness'
        PS =  'PS', 'Pets supplies'
        CG =  'CG', 'Children’s goods'

    title = models.CharField(max_length=50, verbose_name='title' )
    description = models.CharField(null=True, max_length=200, verbose_name='description' )
    starting_bid = models.DecimalField(max_digits=10, decimal_places=1)
    image_url = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=50,choices=Category.choices)
    creation_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True, null=True)
    creator_user = models.ForeignKey(User, on_delete=models.PROTECT)
    buyer = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name="buyer")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    favourite = models.BooleanField(default=True)

class Comment(models.Model):
    description = models.CharField(max_length=500, blank=False, null=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    note = models.CharField(max_length=300, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)