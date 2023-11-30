from django.urls import path
from . import views


urlpatterns = [
  path('' , views.product_catalog , name = 'product_catalog') ,
  path('mens_tshirts/' , views.mens_tshirts , name = 'mens_tshirts') , 
  path('womens_tshirts/' , views.womens_tshirts , name = 'womens_tshirts') ,
  path('kids_tshirts/' , views.kids_tshirts , name = 'kids_tshirts') ,
  path('characters_tshirts/' , views.characters_tshirts , name = 'characters_tshirts') ,
  path('mens_tshirts/<str:brand>/<str:name>/<int:id>/buy' , views.mens_tshirts_overview , name='mens_tshirts_overview') ,
]
