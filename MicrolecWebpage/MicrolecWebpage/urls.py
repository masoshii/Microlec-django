from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
]
