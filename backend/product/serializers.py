from rest_framework import serializers 
from .models import SubCategory,Product,Category

class ProductSerializer(serializers.ModelSerializer):
    category_name=serializers.CharField(source='category.name')
    
    class Meta:
        model=Product
        fields='__all__'


class SubCategorySerializers(serializers.ModelSerializer):
    products=ProductSerializer(many=True,read_only=True)
    class Meta:
        model=SubCategory
        fields='__all__'


class CatogerySerializers(serializers.ModelSerializer):
    sub_catogeries=SubCategorySerializers(many=True, read_only=True)
    products=ProductSerializer(many=True,read_only=True)
    class Meta:
        model=Category
        fields='__all__'

class ProductDetailSeriliser(serializers.ModelSerializer):
    category=CatogerySerializers(read_only=True)
    sub_category=SubCategorySerializers(read_only=True)
    class Meta:
        model=Product
        fields='__all__'