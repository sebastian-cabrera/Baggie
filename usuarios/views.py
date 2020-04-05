from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario

def usuarios(request):
    usr = Usuario.objects.all()
    return render (request, 'usuarios/lista_usuarios.html', {'usuarios': usr})

def alta_usuarios(request):
#    productos = Producto.objects.all()
    return render (request, 'usuarios/form_gestion.html')

def buscar_usuarios(request):
#    productos = Producto.objects.all()
    return render (request, 'usuarios/form_busqueda.html')

def buscar_eliminar_usuarios(request):
#    productos = Producto.objects.all()
    return render (request, 'usuarios/form_busqueda_eliminar.html')


@csrf_exempt
def form_usuarios(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        cedula = request.POST.get('cedula')
        rol = request.POST.get('rol')

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
        usuarios = Usuario.objects.filter(nombre__contains=busqueda)
        return render (request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('usuarios/lista_usuarios.html')
        return HttpResponse(template.render())


@csrf_exempt
def form_buscar_usuario_eliminar(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        usuarios = Usuario.objects.filter(nombre__contains=busqueda)
        return render (request, 'usuarios/lista_usuario_eliminar.html', {'usuarios': usuarios })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('usuarios/lista_usuarios.html')
        return HttpResponse(template.render())


@csrf_exempt
def modificar_usuario(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        usr_id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        cedula = request.POST.get('cedula')
        rol = request.POST.get('rol')

        obj = Usuario.objects.get(id=usr_id)
        obj.nombre = nombre
        obj.email = email
        obj.cedula = cedula
        obj.rol = rol
        obj.save()

        usuario = {
            obj.nombre, obj.email, obj.cedula, obj.rol,
        }

        return render (request, 'usuarios/lista_usuario_modif.html', {'usuario': usuario })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('usuarios/form_gestion.html')
        return HttpResponse(template.render())

@csrf_exempt
def eliminar_usuario(request):
    #if post request came

    if request.method == 'POST':
        #getting values from post
        usr_id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        cedula = request.POST.get('cedula')
        rol = request.POST.get('rol')

        usuario = {
            usr_id, nombre, email, cedula, rol,
        }

        obj = Usuario.objects.get(id=usr_id)
        obj.delete()

        return render (request, 'usuarios/lista_usuario_modif.html', {'usuario': usuario })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('usuarios/form_gestion.html')
        return HttpResponse(template.render())
