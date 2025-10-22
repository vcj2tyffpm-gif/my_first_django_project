from django.shortcuts import render

from .models import Product, Category, Brand

def index(request)
    products = Product.objects.all()
    category = Category.objects.all()
    brand = Brand.oblects.all()

    context = {
        "products"; products,
        "category"; category,
        "brand"; brand,
    }
    
    return render(request, "app/index.html", context=context)