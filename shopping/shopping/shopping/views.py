from django . http import HttpResponse
from django . shortcuts import render
from category . models import Category

def home(request):
    return render(request,"home.html")



def kategori(request):
    return render(request,"kategori.html")

def category(request,kategori_adi):
    return render(request,"kategori.html",{
        "kategori":kategori_adi

    })

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})                                                                                                                                                                                                                                                                      