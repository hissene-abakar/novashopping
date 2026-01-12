from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
def register_view(request):
    if request.method =="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        password2=request.POST.get("password2")
        firstname=request.POST.get("firstname","")
        lastname=request.POST.get("lastname","")
        email=request.POST.get("email")

        if password!=password2:
            messages.warning(request,"sifreniz yanlis!")
            return render(request,"register.html")
        if User.objects.filter(username=username).exists():
            messages.warning(request,"bu kullanci zaten var! ")
            return render(request,"register.html")
        newuser=User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname
        )
        newuser.save()
        return redirect("login")

    return render(request,"register.html")

def logout_view(request):
    logout(request)
    return redirect('login')
    return render(request,'register.html')

def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('anasayfa')
        else:
            messages.error(request,"Kullanıcı bulunamadı")
            return render(request,'login.html')


    return render(request,"login.html")
    

# Create your views here.
