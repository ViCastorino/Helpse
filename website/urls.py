from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('cadastro', views.cadastro),
    path('cadastro_instituicao', views.cadastro_instituicao),
    path('busca_localidade', views.busca_localidade),
    path('busca_especialidade', views.busca_especialidade),
    path('sobre',views.sobre),

]
