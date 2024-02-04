from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import TshirtForm
from .models import Tshirt
from django.views.generic import ListView
from django.views.generic import DetailView


def product_catalog(request):
  return HttpResponse("Hello..")

def create_tshirt(request):
  if request.method == 'POST':
    form = TshirtForm(request.POST, request.FILES)
    if form.is_valid():
      tshirt = form.save()
      # Redirect to the detail view or any other page
      return redirect('home')
  else:
    form = TshirtForm()

  return render(request, 'create_tshirt.html', {'form': form})


def categories(request):
  return render(request , 'categories.html')  

class TshirtListView(ListView):
  model = Tshirt
  template_name = 'tshirt_list.html'  # replace with your template

  def get_queryset(self):
    queryset = super().get_queryset()
    self.category = self.request.GET.get('category')
    self.subcategory = self.request.GET.get('subcategory')
    self.characters = self.request.GET.get('characters')
    self.marvel_subcategory = self.request.GET.get('marvel_subcategory')
    self.dc_comics_subcategory = self.request.GET.get('dc_comics_subcategory')
    self.movies_tv_subcategory = self.request.GET.get('movies_tv_subcategory')
    self.cartoons_anime_subcategory = self.request.GET.get('cartoons_anime_subcategory')
    self.web_series_subcategory = self.request.GET.get('web_series_subcategory')
    self.title = self.request.GET.get('title')
    if self.category:
        queryset = queryset.filter(category=self.category)
    if self.subcategory:
        queryset = queryset.filter(subcategory=self.subcategory)
    if self.characters:
        queryset = queryset.filter(characters=self.characters)
    if self.marvel_subcategory:
        queryset = queryset.filter(marvel_subcategory=self.marvel_subcategory)
    if self.dc_comics_subcategory:
        queryset = queryset.filter(dc_comics_subcategory=self.dc_comics_subcategory)
    if self.movies_tv_subcategory:
        queryset = queryset.filter(movies_tv_subcategory=self.movies_tv_subcategory)
    if self.cartoons_anime_subcategory:
        queryset = queryset.filter(cartoons_anime_subcategory=self.cartoons_anime_subcategory)
    if self.web_series_subcategory:
        queryset = queryset.filter(web_series_subcategory=self.web_series_subcategory)
    if self.title:
        queryset = queryset.filter(brand=self.title) 
    return queryset

  def get_context_data(self, **kwargs):
    self.object_list = self.get_queryset()  # ensure get_queryset is called
    context = super().get_context_data(**kwargs)
    user_id = self.request.session.get('user_id')
    context['user_id'] = user_id
    context['category'] = Tshirt.get_full_name(Tshirt.CATEGORY_CHOICES, self.category)
    context['subcategory'] = Tshirt.get_full_name(Tshirt.SUBCATEGORIES, self.subcategory)
    context['characters'] = Tshirt.get_full_name(Tshirt.CHARACTERS_SUBCATEGORIES, self.characters)
    context['marvel_subcategory'] = Tshirt.get_full_name(Tshirt.MARVEL_SUBCATEGORIES, self.marvel_subcategory)
    context['dc_comics_subcategory'] = Tshirt.get_full_name(Tshirt.DC_COMICS_SUBCATEGORIES, self.dc_comics_subcategory)
    context['movies_tv_subcategory'] = Tshirt.get_full_name(Tshirt.MOVIES_TV_SUBCATEGORIES, self.movies_tv_subcategory)
    context['cartoons_anime_subcategory'] = Tshirt.get_full_name(Tshirt.CARTOONS_ANIME_SUBCATEGORIES, self.cartoons_anime_subcategory)
    context['web_series_subcategory'] = Tshirt.get_full_name(Tshirt.WEB_SERIES_SUBCATEGORIES, self.web_series_subcategory)
    return context

class TshirtDetailView(DetailView):
  model = Tshirt
  template_name = 't-shirts_overview.html' 

  def get_queryset(self):
    queryset = super().get_queryset()
    self.category = self.request.GET.get('category')
    self.subcategory = self.request.GET.get('subcategory')
    self.characters = self.request.GET.get('characters')
    self.marvel_subcategory = self.request.GET.get('marvel_subcategory')
    self.dc_comics_subcategory = self.request.GET.get('dc_comics_subcategory')
    self.movies_tv_subcategory = self.request.GET.get('movies_tv_subcategory')
    self.cartoons_anime_subcategory = self.request.GET.get('cartoons_anime_subcategory')
    self.web_series_subcategory = self.request.GET.get('web_series_subcategory')
    self.title = self.request.GET.get('title')
    if self.category:
        queryset = queryset.filter(category=self.category)
    if self.subcategory:
        queryset = queryset.filter(subcategory=self.subcategory)
    if self.characters:
        queryset = queryset.filter(characters=self.characters)
    if self.marvel_subcategory:
        queryset = queryset.filter(marvel_subcategory=self.marvel_subcategory)
    if self.dc_comics_subcategory:
        queryset = queryset.filter(dc_comics_subcategory=self.dc_comics_subcategory)
    if self.movies_tv_subcategory:
        queryset = queryset.filter(movies_tv_subcategory=self.movies_tv_subcategory)
    if self.cartoons_anime_subcategory:
        queryset = queryset.filter(cartoons_anime_subcategory=self.cartoons_anime_subcategory)
    if self.web_series_subcategory:
        queryset = queryset.filter(web_series_subcategory=self.web_series_subcategory)
    if self.title:
        queryset = queryset.filter(brand=self.title)    
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    tshirt = self.object
    context['tshirt_id'] = tshirt.id
    context['tshirt_details'] = tshirt.name
    context['category'] = Tshirt.get_full_name(Tshirt.CATEGORY_CHOICES, tshirt.category)
    context['subcategory'] = self.request.GET.get('subcategory')
    context['characters'] = self.request.GET.get('characters')
    context['marvel_subcategory'] = self.request.GET.get('marvel_subcategory')
    context['dc_comics_subcategory'] = self.request.GET.get('dc_comics_subcategory')
    context['movies_tv_subcategory'] = self.request.GET.get('movies_tv_subcategory')
    context['cartoons_anime_subcategory'] = self.request.GET.get('cartoons_anime_subcategory')
    context['web_series_subcategory'] = self.request.GET.get('web_series_subcategory')
    return context