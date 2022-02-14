from .models import Listing

def categories_menu(request):
    categories_menu = Listing._meta.get_field('category').choices
    return {'categories_menu': categories_menu }