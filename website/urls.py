from django.urls import path, include
from . import views


urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('cadastro', views.cadastro),
    path('perfil', views.perfil),
    path('quiz', views.quiz),
    path('cadastro_instituicao', views.cadastro_instituicao),
    path('busca_localidade', views.busca_localidade),
    path('busca_especialidade', views.busca_especialidade),
    path('sobre',views.sobre),

]
