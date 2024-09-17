from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    image=models.ImageField(upload_to='categories')
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
        
class SubCategory(models.Model):
    name=models.CharField(max_length=50,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sub_catogeries')
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=128,unique=True)
    image=models.ImageField(upload_to='products')
    description=models.TextField(blank=True,null=True)
    description_detail=models.TextField(blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='products',null=True,help_text="not required")
    # price=models.FloatField()

    def __str__(self) -> str:
        return self.name