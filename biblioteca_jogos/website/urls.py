from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('arquivo/', views.arquivo,name="arquivo"),
    path('pessoas/', views.lista_pessoas, name='lista_pessoa'),
    path('criados.html',views.criados, name='criados'),
    path('criar_post',views.criar_post,name='criar_post')
]