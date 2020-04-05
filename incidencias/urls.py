from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('form_incidencias/', views.form_incidencias),
    path('add/', views.alta_incidencias),
    path('find/', views.form_buscar_incidencias),
    path('modify/', views.gestionar_incidencias),
    path('', views.incidencias),

]
