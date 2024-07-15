from django.contrib import admin
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.urls import include, path
from index import views


urlpatterns = [
    path('contact/', include('contact.urls'), name='contact'),
    path('cart/', include('cart.urls'), name='cart'),
    path('productmgr/', include('product_management.urls'), name='productmgr'),
    path('usermgr/', include('user_management.urls'), name='usermgr'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('category/', include('category.urls'), name='category'),
    path('', include('index.urls'), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.page_not_found

