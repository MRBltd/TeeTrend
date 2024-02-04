from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Wishlist , Cart
from catalog.models import Tshirt
from account.models import UserAccount
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import JsonResponse



def Wishlist_view(request):
  user_id = request.session.get('user_id')
  context = {}
  if 'user_id' in request.session:
    # User is logged in
    user_account = UserAccount.objects.get(id=request.session['user_id'])
    try:
      wishlist = Wishlist.objects.get(user=user_account)
    except ObjectDoesNotExist:
      wishlist = None
    context = {'wishlist': wishlist , 'user_id' : user_id}
  return render(request, 'wishlist.html', context)


def add_to_wishlist(request , title, name, tshirt_id):
  if request.method == 'POST':
    tshirt = get_object_or_404(Tshirt, title=title, name=name, pk=tshirt_id)
    user_account = UserAccount.objects.get(id=request.session['user_id'])
    wishlist, created = Wishlist.objects.get_or_create(user=user_account)
    if wishlist.tshirts.filter(id=tshirt_id).exists():
      return JsonResponse({'message': 'This item is already in your wishlist.'})
    else:
      wishlist.tshirts.add(tshirt)
      return JsonResponse({'message': 'Added to Wishlist'})

def cart_to_wishlist(request , title, name, tshirt_id):
  if request.method == 'POST':
    tshirt = get_object_or_404(Tshirt, title=title, name=name, pk=tshirt_id)
    user_account = UserAccount.objects.get(id=request.session['user_id'])
    wishlist, created = Wishlist.objects.get_or_create(user=user_account)
    cart = Cart.objects.get(user=user_account)
    if wishlist.tshirts.filter(id=tshirt_id).exists():
      return JsonResponse({'message': 'This item is already in your wishlist.'})
    else:
      wishlist.tshirts.add(tshirt)
      if cart.tshirts.filter(id=tshirt_id).exists():
        cart.tshirts.remove(tshirt)
      return JsonResponse({'message': 'Added to Wishlist and removed from Cart'})
  else:
    return HttpResponse('Invalid method')


def remove_from_wishlist(request , tshirt_id):
  tshirt = get_object_or_404(Tshirt, pk=tshirt_id)
  user_account = UserAccount.objects.get(id=request.session['user_id'])
  wishlist = Wishlist.objects.get(user=user_account)
  wishlist.tshirts.remove(tshirt)
  return JsonResponse({'message': 'Item removed from Wishlist'})
  # If the wishlist is empty, delete it
  if not wishlist.tshirts.exists():
    wishlist.delete()
  return JsonResponse({'message': 'Item removed from Wishlist'})

def remove_from_wishlist_nv(request , tshirt_id):
  tshirt = get_object_or_404(Tshirt, pk=tshirt_id)
  user_account = UserAccount.objects.get(id=request.session['user_id'])
  wishlist = Wishlist.objects.get(user=user_account)
  wishlist.tshirts.remove(tshirt)
  return JsonResponse({'message': 'Item removed from Wishlist'})
  # If the wishlist is empty, delete it
  if not wishlist.tshirts.exists():
    wishlist.delete()
  return JsonResponse({'message': 'Item removed from Wishlist'})


def cart_view(request):
  user_id = request.session.get('user_id')
  context = {}
  if 'user_id' in request.session:
    user_account = UserAccount.objects.get(id=request.session['user_id'])
    try:
      cart = Cart.objects.get(user=user_account)
    except ObjectDoesNotExist:
      cart = None
    address = user_account.address
    name = user_account.full_name
    context = {'cart': cart, 'address': address , 'name' : name , 'user_id' : user_id}
  return render(request, 'cart.html', context)  

def add_to_cart(request , title, name, tshirt_id):
  if request.method == 'POST':
    tshirt = get_object_or_404(Tshirt, title=title, name=name, pk=tshirt_id)
    user_account = UserAccount.objects.get(id=request.session['user_id'])
    cart, created = Cart.objects.get_or_create(user=user_account)
    if cart.tshirts.filter(id=tshirt_id).exists():
      return JsonResponse({'message': 'This item is already in your cart.'})
    else:
      cart.tshirts.add(tshirt)
      # Check if the item is in the wishlist and remove it
      wishlist = Wishlist.objects.filter(user=user_account).first()
      if wishlist and wishlist.tshirts.filter(id=tshirt_id).exists():
        wishlist.tshirts.remove(tshirt)
        if not wishlist.tshirts.exists():
          wishlist.delete()
      return JsonResponse({'message': 'Added to Cart'})
  else:
    return HttpResponse('Invalid method')


def remove_from_cart(request, tshirt_id):
  tshirt = get_object_or_404(Tshirt, pk=tshirt_id)
  user_account = UserAccount.objects.get(id=request.session['user_id'])
  cart = Cart.objects.get(user=user_account)
  cart.tshirts.remove(tshirt)
  return JsonResponse({'message': 'Item removed from Cart'})
  # If the cart is empty, delete it
  if not cart.tshirts.exists():
    cart.delete()
  return JsonResponse({'message': 'Item removed from Cart'})