from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__" #모든 필드를 다 불러올 거야/만들거야 

        # exclude = ("creat_at", "update_at", "author", "like_users") #얘네 제외하고!

