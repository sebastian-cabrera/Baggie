from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('form_operaciones/', views.form_operaciones),
    path('add/', views.alta_operaciones),
    path('find/', views.form_buscar_operaciones),
    path('modify/', views.gestionar_operaciones),
    path('', views.operaciones),

]
