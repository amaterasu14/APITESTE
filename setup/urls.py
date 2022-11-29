from django.contrib import admin
from django.urls import path, include
from apifaculdade.views import SenhaViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('senha', SenhaViewSet, basename='Senha')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls))
    ]
