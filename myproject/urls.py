from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Точка означает: зайди в папку products и найди там файл urls.py
    path('products/', include('products.urls')), 
]
