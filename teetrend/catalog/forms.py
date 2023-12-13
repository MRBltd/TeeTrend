from django import forms
from .models import Tshirt

class TshirtForm(forms.ModelForm):
  class Meta:
    model = Tshirt
    fields = '__all__'

    labels = {
        'characters' : 'Characters Subcategory' ,
        'name' : 'T-shirt Name' ,
        'description' : 'T-shirt Details' ,
        'price' : 'T-shirt Price' ,
        'image' : 'Sample Images(do not give the first field blank.)' ,
        'image1' : 'ii' ,
        'image2' : 'iii' ,
        'image3' : 'iv' ,
        'image4' : 'v' ,
        'image5' : 'vi' ,
        'image6' : 'vii' ,
        'image7' : 'viii' ,
      }