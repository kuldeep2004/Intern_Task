from django.contrib import admin
from django.urls import path,include
from prod.fetched import fetch_and_store_products,remove_duplicate_images
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prod.urls')),
]

fetch_and_store_products()
remove_duplicate_images()