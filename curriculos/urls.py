from django.urls import path
from . import views

urlpatterns = [
    path('', views.listagem, name='listagem'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('curriculo/<int:pk>/', views.consulta, name='consulta'),
]