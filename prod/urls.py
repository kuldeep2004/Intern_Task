from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.index, name='index'),
    path('api/<int:pid>/', views.detail, name='detail'),
    path('products/', views.products, name='products'),
    path('products/<str:category>/<str:brand>/<str:title>/<int:pid>/', views.product, name='product'),
]