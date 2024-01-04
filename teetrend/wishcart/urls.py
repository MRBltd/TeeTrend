from django.urls import path
from . import views

urlpatterns = [
  path('wishlist/' , views.Wishlist_view , name = 'wishlist_view') ,
  path('add_to_wishlist/<int:tshirt_id>/', views.add_to_wishlist, name='add_to_wishlist') ,
  path('remove_from_wishlist/<int:tshirt_id>/', views.remove_from_wishlist, name='remove_from_wishlist') ,
]