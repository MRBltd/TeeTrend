from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from wishcart.models import Cart
from catalog.models import Tshirt
from account.models import UserAccount
from .models import Payment
import stripe


def address(request):
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
  return render(request , 'address.html' , context)

def payment(request):
  context = {}
  if 'user_id' in request.session:
    # User is logged in
    user_account = UserAccount.objects.get(id=request.session['user_id'])
    try:
      cart = Cart.objects.get(user=user_account)
    except ObjectDoesNotExist:
      cart = None
    context = {'cart': cart}
  return render(request , 'payment.html' , context)

def make_payment(request):
  if request.method == 'POST':
    # Get the payment amount from the form
    amount = request.POST['amount']
    user_account = UserAccount.objects.get(id=request.session['user_id'])
    # Create a new payment
    payment = Payment(user=user_account, amount=amount, status='Pending')
    payment.save()
    print(payment)
    # Process the payment using Stripe's API
    stripe.api_key = 'your_stripe_secret_key'
    stripeToken = request.POST.get('stripeToken')
    if stripeToken is not None:
        charge = stripe.Charge.create(
          amount=int(float(amount) * 100),  # Stripe expects the amount in paise for INR
          currency='inr',  # Changed from 'usd' to 'inr'
          description='Example charge',
          source=stripeToken,
        )
        # Update the payment status based on the response from Stripe
        if charge['paid']:
          payment.status = 'Paid'
          payment.save()
    else:
      # Handle the case where stripeToken is not provided
      # You might want to return an error message to the user
      return render(request, 'error.html', {'message': 'Stripe token not provided'})
    return render(request, 'success_payment.html')
  return render(request, 'make_payment.html')