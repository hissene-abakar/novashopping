from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('shop.urls')),
    path('', views.home, name="anasayfa"),
    path('category/', include('category.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

# Servir les fichiers media (images) en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)