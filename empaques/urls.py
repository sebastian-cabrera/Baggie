from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/form_empaques/', views.form_empaques),
    path('add/', views.alta_empaques),
    path('find/', views.form_buscar_empaques),
    path('modify/', views.gestionar_empaques),
    path('', views.empaques),

]
