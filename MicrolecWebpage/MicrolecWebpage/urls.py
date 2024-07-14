from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('contact/', include('contact.urls')),
    path('cart/', include('cart.urls')),
    path('productmgr/', include('product_management.urls')),
    path('usermgr/', include('user_management.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('index.urls')),
]
