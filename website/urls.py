from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('cadastro', views.cadastro),
    path('cadastro_instituicao', views.cadastro_instituicao),
    path('agendar', views.agendar),
    path('sobre',views.sobre),

]
