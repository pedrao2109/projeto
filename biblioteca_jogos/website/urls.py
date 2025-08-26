from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('arquivo/', views.arquivo,name="arquivo"),
    path('pessoas/', views.lista_pessoas, name='lista_pessoa'),
]