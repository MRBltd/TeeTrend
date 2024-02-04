from django.urls import path
from . import views

urlpatterns = [
  # Wishlist
  path('wishlist/' , views.Wishlist_view , name='wishlist_view') ,
  path('add_to_wishlist/<str:title>/<str:name>/<int:tshirt_id>/', views.add_to_wishlist, name='add_to_wishlist') ,
  path('checkout/cart/cart_to_wishlist/<str:title>/<str:name>/<int:tshirt_id>/' , views.cart_to_wishlist , name='cart_to_wishlist') ,
  path('remove_from_wishlist/<int:tshirt_id>/', views.remove_from_wishlist, name='remove_from_wishlist') ,
  path('wishlist/remove_from_wishlist_nv/<int:tshirt_id>/' , views.remove_from_wishlist_nv , name='remove_from_wishlist_nv') ,
  # Cart
  path('checkout/cart/' , views.cart_view , name='cart_view') ,
  path('wishlist/add_to_cart/<str:title>/<str:name>/<int:tshirt_id>/' , views.add_to_cart , name='add_to_cart') ,
  path('checkout/cart/remove_from_cart/<int:tshirt_id>/' , views.remove_from_cart , name='remove_from_cart') ,
]