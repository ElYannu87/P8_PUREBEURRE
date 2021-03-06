from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Favorite
from users.models import User
from products.models import Product

# Create your views here.

# user has to be logged if he want to see favorites


@login_required(login_url='login')
def user_favorites(request):
    """
    Allows a user to see their favorites
    """
    user = request.user
    user_favorites_set = Favorite.objects.get_favorites_from_user(user)
    return render(request, "favorites/favorites.html", {"favorites":
                                                        user_favorites_set})


@login_required(login_url='login')
def add_favorite(request, product_id, substitute_id):
    """
    Allows a user to save their favorites and to save them into the database
    """
    user = request.user
    try:
        product, substitute = (Product.objects.get(barcode=product_id),
                               Product.objects.get(barcode=substitute_id))
    except (IntegrityError, Product.DoesNotExist):
        # if the product or substitute doesn't exist
        messages.info(request, "Produit ou substitut inexistant !")
        return redirect('/')
    favorite = Favorite(user=user, product=product, substitute=substitute)
    try:
        favorite.save()
    except IntegrityError:
        # if tuple (product, substitute) is already save as favorite
        messages.info(request, "Ce favori existe déjà !")
        return redirect('/')

    return redirect("user_favorites")
