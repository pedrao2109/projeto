from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('arquivo/', views.arquivo,name="arquivo"),
    path('pessoas/', views.lista_pessoas, name='lista_pessoa'),
    path('criados/',views.criados, name='criados'),
    path('criar_post/',views.criar_post,name='criar_post'),
    path('carrossel/',views.carrossel, name='carrossel'),
    path('recomendados/',views.recomendados, name='recomendados'),
    path('sobre/',views.sobre, name='sobre')
]