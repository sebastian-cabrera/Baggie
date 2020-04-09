from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('form_productos/', views.form_productos),
    path('add/', views.alta_productos),
    path('find/', views.form_buscar_productos),
    path('modify/', views.gestionar_producto),
    path('', views.productos),

]
