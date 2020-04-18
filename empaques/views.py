from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Empaque

def empaques(request):
    pak = Empaque.objects.all()
    return render (request, 'empaques/lista_empaques.html', {'empaques': pak})

def alta_empaques(request):
    return render (request, 'empaques/form_gestion.html')



###############################################################################
#
#       Objetivo:   Funcion para gestion de empaques
#       Sustituye:  form_empaques(request)
#                   modificar_empaque(request):
#                   eliminar_empaque(request):
#
##############################################################################


@csrf_exempt
def gestionar_empaques(request):
    if request.method == 'POST':
        pak_id = request.POST.get('id')
        tipo = request.POST.get('tipo')
        proveedor = request.POST.get('proveedor')
        modelo = request.POST.get('modelo')
        dimensiones = request.POST.get('dimensiones')
        peso_max = request.POST.get('peso_max')
        cantidad_usos = request.POST.get('cantidad_usos')
        accion = request.POST.get('accion')

        empaques = {
            pak_id, tipo, proveedor,
            modelo, dimensiones, peso_max,
            cantidad_usos, accion
        }

        if  accion == 'Modificar':
            obj = Empaque.objects.get(id=pak_id)
            obj.Tipo = tipo
            obj.Proveedor = proveedor
            obj.modelo = modelo
            obj.Dimensiones = dimensiones
            obj.Peso_Max = peso_max
            obj.Cantidad_Usos = cantidad_usos
            obj.save()
            return render (request, 'empaques/lista_empaque_modif.html', {'empaques': empaques})

        elif accion == 'Borrar':
            obj = Empaque.objects.get(id=pak_id)
            obj.delete()
            return render (request, 'empaques/lista_empaque_modif.html', {'empaques': empaques})
        else:
            return render (request, 'empaques/lista_empaque_modif.html')



@csrf_exempt
def form_buscar_empaques(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        empaques = Empaque.objects.filter(Tipo__contains=busqueda)
        return render (request, 'empaques/lista_empaques.html', {'empaques': empaques })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('usuarios/lista_usuarios.html')
        return HttpResponse(template.render())

###############################################################################
#
#       Obsoleto:   Funcion para buscar empaque para eliminar
#       Sustituta:  gestion_empaques()
#

@csrf_exempt
def form_buscar_empaques_eliminar(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        empaques = Empaque.objects.filter(Tipo__contains=busqueda)
        return render (request, 'empaques/lista_empaque_eliminar.html', {'empaques': empaques })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('empaques/lista_empaques.html')
        return HttpResponse(template.render())

###############################################################################
#
#       Obsoleto:   Funcion para alta de empaque
#       Sustituta:  gestion_empaques()
#

@csrf_exempt
def form_empaques(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        tipo = request.POST.get('tipo')
        proveedor = request.POST.get('proveedor')
        modelo = request.POST.get('modelo')
        dimensiones = request.POST.get('dimensiones')
        peso_max = request.POST.get('peso_max')
        cantidad_usos = request.POST.get('cantidad_usos')

        obj = Empaque()
        obj.Tipo = tipo
        obj.Proveedor = proveedor
        obj.Modelo = modelo
        obj.Dimensiones = dimensiones
        obj.Peso_Max = peso_max
        obj.Cantidad_Usos = cantidad_usos
        obj.save()

        empaques = {
            obj.id,
            obj.Tipo,
            obj.Proveedor,
            obj.Modelo,
            obj.Dimensiones,
            obj.Peso_Max,
            obj.Cantidad_Usos
        }

        return render (request, 'empaques/lista_empaque_modif.html', {'empaques': empaques})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('empaques/form_gestion.html')
        return HttpResponse(template.render())

###############################################################################
#
#       Obsoleto:   Funcion para modificar un empaque
#       Sustituta:  gestion_empaques()
#

@csrf_exempt
def modificar_empaque(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        pak_id = request.POST.get('id')
        tipo = request.POST.get('tipo')
        proveedor = request.POST.get('proveedor')
        modelo = request.POST.get('modelo')
        dimensiones = request.POST.get('dimensiones')
        peso_max = request.POST.get('peso_max')
        cantidad_usos = request.POST.get('cantidad_usos')

        obj = Empaque.objects.get(id=pak_id)
        obj.Tipo = tipo
        obj.Proveedor = proveedor
        obj.modelo = modelo
        obj.Dimensiones = dimensiones
        obj.Peso_Max = peso_max
        obj.Cantidad_Usos = cantidad_usos
        obj.save()

        empaque = {
            obj.id, obj.Tipo, obj.Proveedor,
            obj.modelo, obj.Dimensiones, obj.Peso_Max,
            obj.Cantidad_Usos
        }

        return render (request, 'empaques/lista_empaque_modif.html', {'empaque': empaque})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('empaques/form_gestion.html')
        return HttpResponse(template.render())

###############################################################################
#
#       Obsoleto:   Funcion para eliminar un empaque
#       Sustituta:  gestion_empaques()
#
@csrf_exempt
def eliminar_empaque(request):
    #if post request came

    if request.method == 'POST':
        #getting values from post
        prod_id = request.POST.get('id')
        tipo = request.POST.get('tipo')
        proveedor = request.POST.get('proveedor')
        modelo = request.POST.get('modelo')
        dimensiones = request.POST.get('dimensiones')
        peso_max = request.POST.get('peso_max')
        cantidad_usos = request.POST.get('cantidad_usos')

        empaque = {
                    prod_id,
                    tipo,
                    proveedor,
                    modelo,
                    dimensiones,
                    peso_max,
                    cantidad_usos,
        }

        obj = Empaque.objects.get(id=prod_id)
        obj.delete()

        return render (request, 'empaques/lista_empaque_modif.html', {'empaques': empaque})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('empaques/form_gestion.html')
        return HttpResponse(template.render())
