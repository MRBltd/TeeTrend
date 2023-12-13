from django.contrib import admin
from .models import Tshirt



class TshirtAdmin(admin.ModelAdmin):
  list_display = ['title' , 'name', 'price', 'image', 'image1' , 'image2' , 'image3' , 'image4' , 'image5' , 'image6' , 'image7' , 'category', 'stock', 'discount', 'size', 'color', 'material', 'brand']
  search_fields = ['name', 'description']

admin.site.register(Tshirt, TshirtAdmin)