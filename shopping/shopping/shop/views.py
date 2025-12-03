from django.shortcuts import render
def home(request):
    return render(request,"home.html")

def kategori(request):
    return render(request,"kategori.html")

# Create your views here.
