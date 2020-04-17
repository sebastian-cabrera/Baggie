from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
#   path('form_usuarios/', views.form_usuarios),
    path('add/', views.alta_usuarios),
    path('find/', views.form_buscar_usuarios),
    path('modify/', views.gestionar_usuario),
    path('', views.usuarios),

]
