from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Usuario

def usuarios(request):
    usr = User.objects.all()
    return render (request, 'usuarios/lista_usuarios.html', {'usuarios': usr})




def alta_usuarios(request):
    return render (request, 'usuarios/form_gestion.html')

def buscar_usuarios(request):
    return render (request, 'usuarios/form_busqueda.html')


@csrf_exempt
def form_usuarios(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        apellido = request.POST.get('apellido')


        obj = Usuario()
        obj.nombre = nombre
        obj.email = email
        obj.cedula = cedula
        obj.rol = rol
        obj.save()

        usuarios = Usuario.objects.all()
        return render (request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('usuarios/form_gestion.html')
        return HttpResponse(template.render())



@csrf_exempt
def form_buscar_usuarios(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        usuarios = User.objects.filter(username__contains=busqueda)
        return render (request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('usuarios/lista_usuarios.html')
        return HttpResponse(template.render())


@csrf_exempt
def gestionar_usuario(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        usuario = request.POST.get('usuario')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        accion = request.POST.get('accion')

        usuarios = {
            usuario, nombre, apellido, email
        }

        if accion == "Modificar":
            obj = User.objects.get(username = usuario)
            obj.first_name = nombre
            obj.last_name = apellido
            obj.email = email
            obj.save()

            return render (request, 'usuarios/lista_usuario_modif.html', {'usuarios': usuarios })

        elif accion == "Borrar":

            obj = User.objects.get(username = usuario)
            obj.delete()

            return render (request, 'usuarios/lista_usuario_modif.html', {'usuarios': usuarios })

        else:
            return render (request, 'usuarios/lista_usuarios.html')

    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('usuarios/form_gestion.html')
        return HttpResponse(template.render())
