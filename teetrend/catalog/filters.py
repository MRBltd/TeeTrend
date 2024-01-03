import django_filters as filters
from .models import Tshirt

class MyModelFilterSet(filters.FilterSet):
  class Meta:
    model = Tshirt
    fields = ['category', 'subcategory', 'characters', 'marvel_subcategory', 'dc_comics_subcategory', 'movies_tv_subcategory', 'cartoons_anime_subcategory', 'web_series_subcategory', 'title', 'name', 'price', 'age', 'size', 'color', 'material', 'brand', 'discount']