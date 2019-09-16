from django.urls import path
from .views import (cargar_inicio,politicas,LoginView, LogoutView)

urlpatterns = [
    path('', cargar_inicio, name = 'inicio'),
    path('politicas/',politicas,name ='politicas'),

    path('login/', LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logoutsesion', LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),

]