from django . http import HttpResponse
from django . shortcuts import render

def home(request):
    return render(request,"home.html")

def kategori(request):
    return render(request,"kategori.html")
