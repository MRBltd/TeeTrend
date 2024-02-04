from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home.urls')) ,
    path('account/' , include('account.urls')) ,
    path('' , include('catalog.urls')) ,
    path('tshirt/' , include('wishcart.urls')) ,
    path('tshirt/' , include('paymentgateway.urls')) ,
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
