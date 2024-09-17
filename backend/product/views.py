from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import CatogerySerializers, ProductDetailSeriliser, ProductSerializer
from .models import Category, Product
# Create your views here.
@api_view(['GET'])
def get_categories(request):
    data=CatogerySerializers(Category.objects.all(),many=True).data
    return JsonResponse({'data':data})

@api_view(['GET','OPTIONS'])
def get_category(request,name):
    
    print(id)
    data=CatogerySerializers(Category.objects.get(name=name)).data
    print(data)
    return JsonResponse({'data':data})

@api_view(['GET','OPTIONS'])
def get_product(request,name):
    
    print(id)
    data=ProductDetailSeriliser(Product.objects.get(name=name)).data
    print(data)
    return JsonResponse({'data':data})