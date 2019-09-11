from django.urls import path
from .views import (cargar_inicio,a,LoginView, LogoutView)

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('a/',a,name ='a'),

]