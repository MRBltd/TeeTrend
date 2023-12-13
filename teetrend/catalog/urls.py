from django.urls import path
from . import views
from .views import TshirtListView , TshirtDetailView


urlpatterns = [
  path('' , views.product_catalog , name = 'product_catalog') ,
  path('create/' , views.create_tshirt , name = 'create_tshirt') ,
  path('categories/' , views.categories , name = 'categories') ,
  path('tshirts/', TshirtListView.as_view(), name='tshirt_list') ,
  path('tshirts/<int:pk>/', TshirtDetailView.as_view(), name='tshirt_detail') ,
]