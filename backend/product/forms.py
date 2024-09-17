from django import forms

from .models import Product,Category, SubCategory

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Category")
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects.all(), required=False, label="Sub-Category")

    class Meta:
        model = Product
        fields = '__all__'
