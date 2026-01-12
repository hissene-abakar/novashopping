from django.shortcuts import render
from category.models import Category
def home(request):
    categories = Category.objects.prefetch_related("products")
    return render(request,"home.html", {
        "categories": categories
    })


def kategori(request):
    categories = Category.objects.prefetch_related("products")
    return render(request, "kategori.html", {
        "categories": categories
    })