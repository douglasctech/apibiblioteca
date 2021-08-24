from django.contrib import admin
from django.urls import path, include
from bibliotecaapp.views import LivrosViewSet
from rest_framework import routers

router1 = routers.DefaultRouter()
router1.register(r'livros', LivrosViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router1.urls)),
    
]
