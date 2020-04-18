from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Producto

@login_required
def productos(request):
    productos = Producto.objects.all()
    return render (request, 'productos/lista_productos.html', {'productos': productos})


@login_required
def alta_productos(request):
#    productos = Producto.objects.all()
    return render (request, 'productos/form_gestion.html')


@login_required
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


@login_required
@csrf_exempt
def form_productos(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        nombre = request.POST.get('nombre')
        variedad = request.POST.get('variedad')
        procedencia = request.POST.get('procedencia')
        zafra = request.POST.get('zafra')
        tipo = request.POST.get('tipo')

        obj = Producto()
        obj.Nombre = nombre
        obj.Variedad = variedad
        obj.Procedencia = procedencia
        obj.Zafra = zafra
        obj.Tipo = tipo
        obj.save()

        productos = {
            nombre, variedad, procedencia, zafra, tipo
        }
        return render (request, 'productos/lista_producto_modif.html', {'productos': productos})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('productos/form_gestion.html')
        return HttpResponse(template.render())



##############################################################################
#
#   Objetivo: Funcion para modificar y eliminar productos
#
@login_required
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

        productos = {
            prod_id, nombre, variedad,
            procedencia, zafra, tipo
        }

        if accion == 'Modificar':
            obj = Producto.objects.get(id=prod_id)
            obj.Nombre = nombre
            obj.Variedad = variedad
            obj.Procedencia = procedencia
            obj.Zafra = zafra
            obj.Tipo = tipo
            obj.save()

            return render (request, 'productos/lista_producto_modif.html', {'productos': productos})

        elif accion == 'Borrar':

            obj = Producto.objects.get(id=prod_id)
            obj.delete()

            return render (request, 'productos/lista_producto_modif.html', {'productos': productos})
        else:
            return render (request, 'productos/lista_productos.html')
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('productos/form_gestion.html')
        return HttpResponse(template.render())
