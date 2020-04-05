from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Producto


def productos(request):
    productos = Producto.objects.all()
    return render (request, 'productos/lista_productos.html', {'productos': productos})

def alta_productos(request):
#    productos = Producto.objects.all()
    return render (request, 'productos/form_gestion.html')
"""
def buscar_productos(request):
#    productos = Producto.objects.all()
    return render (request, 'productos/form_busqueda.html')

def buscar_eliminar_productos(request):
#    productos = Producto.objects.all()
    return render (request, 'productos/form_busqueda_eliminar.html')
"""
@csrf_exempt
def form_buscar_productos(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        productos = Producto.objects.filter(Nombre__contains=busqueda)
        return render (request, 'productos/lista_productos.html', {'productos': productos })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('usuarios/lista_usuarios.html')
        return HttpResponse(template.render())
"""
@csrf_exempt
def form_buscar_productos_eliminar(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        productos = Producto.objects.filter(Nombre__contains=busqueda)
        return render (request, 'productos/lista_producto_eliminar.html', {'productos': productos })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('productos/lista_productos.html')
        return HttpResponse(template.render())
"""
@csrf_exempt
def form_productos(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        nombre = request.POST.get('nombre')
        variedad = request.POST.get('variedad')
        procedencia = request.POST.get('procedencia')
        zafra = request.POST.get('zafra')

        obj = Producto()
        obj.Nombre = nombre
        obj.Variedad = variedad
        obj.Procedencia = procedencia
        obj.Zafra = zafra
        obj.save()

        productos = Producto.objects.all()
        return render (request, 'productos/lista_producto_modif.html', {'productos': productos})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('productos/form_gestion.html')
        return HttpResponse(template.render())
"""
@csrf_exempt
def modificar_producto(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        prod_id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        variedad = request.POST.get('variedad')
        procedencia = request.POST.get('procedencia')
        zafra = request.POST.get('zafra')
        tipo = request.POST.get('tipo')

        obj = Producto.objects.get(id=prod_id)
        obj.Nombre = nombre
        obj.Variedad = variedad
        obj.Procedencia = procedencia
        obj.Zafra = zafra
        obj.Tipo = tipo
        obj.save()

        productos = Producto.objects.all()
        return render (request, 'productos/lista_producto_modif.html', {'productos': productos})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('productos/form_gestion.html')
        return HttpResponse(template.render())
"""
###
"""
#
#   Funcion para eliminacion de Productos
#

@csrf_exempt
def eliminar_producto(request):
    #if post request came

    if request.method == 'POST':
        #getting values from post
        prod_id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        variedad = request.POST.get('variedad')
        procedencia = request.POST.get('procedencia')
        zafra = request.POST.get('zafra')
        tipo = request.POST.get('tipo')
        producto = {
            prod_id, nombre, variedad, procedencia, zafra, tipo,
        }

        obj = Producto.objects.get(id=prod_id)
        obj.delete()

        return render (request, 'productos/lista_producto_modif.html', {'producto': producto})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('productos/form_gestion.html')
        return HttpResponse(template.render())
"""


##############################################################################
#
#   Objetivo: Funcion para modificar y eliminar productos
#

@csrf_exempt
def gestionar_producto(request):
    if request.method == 'POST':
        #getting values from post
        prod_id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        variedad = request.POST.get('variedad')
        procedencia = request.POST.get('procedencia')
        zafra = request.POST.get('zafra')
        tipo = request.POST.get('tipo')
        accion = request.POST.get('accion')

        if accion == 'Modificar':
            obj = Producto.objects.get(id=prod_id)
            obj.Nombre = nombre
            obj.Variedad = variedad
            obj.Procedencia = procedencia
            obj.Zafra = zafra
            obj.Tipo = tipo
            obj.save()

            producto = {
                obj.Nombre, obj.Variedad, obj.Procedencia, obj.Zafra, obj.Tipo
            }

            return render (request, 'productos/lista_producto_modif.html', {'producto': producto})

        elif accion == 'Borrar':

            producto = {
                prod_id, nombre, variedad, procedencia, zafra, tipo,
            }

            obj = Producto.objects.get(id=prod_id)
            obj.delete()

            return render (request, 'productos/lista_producto_modif.html', {'producto': producto})
        else:
            return render (request, 'productos/lista_productos.html')
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('productos/form_gestion.html')
        return HttpResponse(template.render())
