from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse as JSONResponse
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import render, get_object_or_404
import requests

# Create your views here.
@api_view(['GET'])
def index(request):
    skip = int(request.GET.get('skip', 0))
    limit = int(request.GET.get('limit', 10))
    products = Product.objects.all()[skip:skip+limit]
    serializer = ProductSerializer(products, many=True)
    response= JSONResponse({'products': serializer.data, 'total': Product.objects.count(), 'skip': skip, 'limit': limit})
    response["Access-Control-Allow-Origin"]="*"
    response["Access-Control-Allow-Methods"]="GET,OPTIONS"
    response["Access-Control-Max-Age"]="1000"
    response["Access-Control-Allow-Headers"]="X-Requested-With,Content-Type"
    return response

@api_view(['GET'])
def detail(request,pid):
    try:
        product = Product.objects.get(id=pid)
        serializer = ProductSerializer(product)
        return JSONResponse(serializer.data)
    except Product.DoesNotExist:
        return JSONResponse({'error': 'Product not found'}, status=404)

def products(request):
    return render(request, 'products.html')

def product(request,category,brand,title,pid):
    context={'prod_id':pid,'category':category,'brand':brand,'title':title}
    return render(request, 'product.html',{'param':context})
    
    
