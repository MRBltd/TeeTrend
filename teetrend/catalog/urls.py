from django.urls import path
from . import views


urlpatterns = [
  path('' , views.product_catalog , name = 'product_catalog') ,
  path('mens_tshirts/' , views.mens_tshirts , name = 'mens_tshirts')
]
