from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/form_usuarios/', views.form_usuarios),
    path('add/', views.alta_usuarios),
#    path('find/fbu/del/', views.eliminar_usuario),
    path('find/', views.form_buscar_usuarios),
#    path('find/', views.buscar_usuarios),
    path('delete/feu/del/', views.eliminar_usuario),
    path('delete/feu/', views.form_buscar_usuario_eliminar),
    path('delete/', views.buscar_eliminar_usuarios),
    path('modify/', views.modificar_usuario),
    path('', views.usuarios),

]
