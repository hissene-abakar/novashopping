from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="shop"),
    path('kategori/',views.kategori,name='kategori'),  
]
