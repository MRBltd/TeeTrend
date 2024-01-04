from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from catalog.models import Tshirt
from account.models import UserAccount
from django.core.exceptions import ObjectDoesNotExist



def Wishlist_view(request):
  if 'user_id' in request.session:
    # User is logged in
    user_account = UserAccount.objects.get(id=request.session['user_id'])
    try:
      wishlist = Wishlist.objects.get(user=user_account)
    except ObjectDoesNotExist:
      wishlist = None
    context = {'wishlist': wishlist}
    return render(request, 'wishlist.html', context)
  else:
    # User is not logged in, redirect to the sign-in page
    return redirect('sign_in')


@login_required
def add_to_wishlist(request, tshirt_id):
  tshirt = get_object_or_404(Tshirt, pk=tshirt_id)
  if 'user_id' in request.session:
    user_account = UserAccount.objects.get(id=request.session['user_id'])
    print(user_account)
    wishlist, created = Wishlist.objects.get_or_create(user=user_account)
    wishlist.tshirts.add(tshirt)
    print(wishlist)
    return redirect('wishlist_view')
  else:
    # User is not logged in, redirect to the sign-in page
    return redirect('sign_in')  

@login_required
def remove_from_wishlist(request, tshirt_id):
  tshirt = get_object_or_404(Tshirt, pk=tshirt_id)
  user_account = UserAccount.objects.get(id=request.session['user_id'])
  wishlist = Wishlist.objects.get(user=user_account)
  wishlist.tshirts.remove(tshirt)
  # If the wishlist is empty, delete it
  if not wishlist.tshirts.exists():
    wishlist.delete()
  return redirect('wishlist_view')  