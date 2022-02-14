from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("", views.index, name="index"),
    # for active, favourites, won, or own auctions list
    path("auctions/<filter>/<cat>", views.auctions_list, name="auctions_list"),
    path("auction/<str:id>", views.show_auction, name="show_auction"),
    path("create_auction", views.create_auction, name="create_auction"),

    path("favourite/<str:listing>/<str:user>", views.favourite, name="favourite"),
    path("activate/<str:listing>", views.activate, name="activate"),

] 