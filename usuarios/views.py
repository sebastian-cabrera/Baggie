from.django.http import HttpResponse
from django.shortcuts import render
from.models import Usuario

def usuarios(request):
    usuarios = Usuario.objects.all()
    lista_usuarios = "- ".join(usuarios)
    return HttpResponse(lista_usuarios)
