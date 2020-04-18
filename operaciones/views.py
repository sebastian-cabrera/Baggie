from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Movimiento, Empaque, Producto
from django.contrib.auth.models import User

@login_required
def operaciones(request):
    operaciones = Movimiento.objects.all()
    return render (request, 'operaciones/lista_operaciones.html', {'operaciones': operaciones})


@login_required
def alta_operaciones(request):
#    productos = Producto.objects.all()
    return render (request, 'operaciones/form_gestion.html')


@login_required
@csrf_exempt
def gestionar_operaciones(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        # Cuando vamos a grabar en un campo que es clave foranea, debemos hacer una instancia de dicho atributo.
        id_empaque = Empaque.objects.get(id=request.POST.get('id_empaque'))
        id_producto = Producto.objects.get(id=request.POST.get('id_producto'))
        id_usuario = Usuario.objects.get(id=request.POST.get('id_usuario'))
        accion = request.POST.get('accion')

        if accion == 'Modificar':
            obj = Movimiento()
            obj.Descripcion = descripcion
            obj.ID_Empaque = id_empaque
            obj.ID_Producto = id_producto
            obj.ID_Usuario = id_usuario
            obj.save()

            operacion = {
                obj.Descripcion,
                obj.ID_Empaque,
                obj.ID_Producto,
                obj.ID_Usuario
            }

            return render (request, 'operaciones/lista_operacion_modif.html', {'operacion': operacion})

        elif accion == 'Borrar':
            operacion = {
                prod_id, nombre, variedad, procedencia, zafra, tipo,
            }

            obj = Movimiento.objects.get(id=op_id)
            obj.delete()

            return render (request, 'operaciones/lista_operaciones.html', {'operacion': operacion})

        else:
            return render (request, 'operaciones/lista_operaciones.html')

    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('operaciones/form_gestion.html')
        return HttpResponse(template.render())



@login_required
@csrf_exempt
def form_buscar_operaciones(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        operaciones = Movimiento.objects.filter(Descripcion__contains=busqueda)
        return render (request, 'operaciones/lista_operaciones.html', {'operaciones': operaciones})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('operaciones/lista_operaciones.html')
        return HttpResponse(template.render())


"""
@csrf_exempt
def form_buscar_operaciones_eliminar(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        operaciones = Movimiento.objects.filter(Descripcion__contains=busqueda)
        return render (request, 'operaciones/lista_operaciones_eliminar.html', {'operaciones': operaciones })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('operaciones/lista_operaciones.html')
        return HttpResponse(template.render())

"""

##############################################################################
#
#

@login_required
@csrf_exempt
def form_operaciones(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        descripcion = request.POST.get('descripcion')

        # Cuando vamos a grabar en un campo que es clave foranea, debemos hacer una instancia de dicho atributo.
        id_empaque = Empaque.objects.get(id=request.POST.get('id_empaque'))
        id_producto = Producto.objects.get(id=request.POST.get('id_producto'))
        id_usuario = Usuario.objects.get(id=request.POST.get('id_usuario'))

        obj = Movimiento()
        obj.Descripcion = descripcion
        obj.ID_Empaque = id_empaque
        obj.ID_Producto = id_producto
        obj.ID_Usuario = id_usuario
        obj.save()

        operacion = {
            obj.Descripcion,
            obj.ID_Empaque,
            obj.ID_Producto,
            obj.ID_Usuario
        }
        return render (request, 'operaciones/lista_operacion_modif.html', {'operacion': operacion})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('operaciones/form_gestion.html')
        return HttpResponse(template.render())

"""
##############################################################################
@csrf_exempt
def modificar_operacion(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        op_id = request.POST.get('id')
        descripcion = request.POST.get('descripcion')
        id_empaque = Empaque.objects.get(id=request.POST.get('id_empaque'))
        id_producto = Producto.objects.get(id=request.POST.get('id_producto'))
        id_usuario = Usuario.objects.get(id=request.POST.get('id_usuario'))

        obj = Movimiento.objects.get(id=op_id)
        obj.Descripcion = descripcion
        obj.ID_Empaque = id_empaque
        obj.ID_Producto = id_producto
        obj.ID_Usuario = id_usuario
        obj.save()

        operacion = {
            obj.Descripcion,
            obj.ID_Empaque,
            obj.ID_Producto,
            obj.ID_Usuario
        }
        return render (request, 'operaciones/lista_operacion_modif.html', {'operacion': operacion})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('operaciones/form_gestion.html')
        return HttpResponse(template.render())

#
#   Funcion para eliminacion de Productos
#

@csrf_exempt
def eliminar_operacion(request):
    #if post request came

    if request.method == 'POST':
        #getting values from post
        op_id = request.POST.get('id')
        descripcion = request.POST.get('descripcion')
        id_empaque = Empaque.objects.get(id=request.POST.get('id_empaque'))
        id_producto = Producto.objects.get(id=request.POST.get('id_producto'))
        id_usuario = Usuario.objects.get(id=request.POST.get('id_usuario'))

        operacion = {
            prod_id, nombre, variedad, procedencia, zafra, tipo,
        }

        obj = Movimiento.objects.get(id=op_id)
        obj.delete()

        return render (request, 'operaciones/lista_operaciones.html', {'operacion': operacion})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('operaciones/form_gestion.html')
        return HttpResponse(template.render())
"""
