from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Incidencia, Empaque, Producto, Usuario

def incidencias(request):
    inc = Incidencia.objects.all()
    return render (request, 'incidencias/lista_incidencias.html', {'incidencias': inc})

def alta_incidencias(request):
#    inc = Incidencia.objects.all()
    return render (request, 'incidencias/form_gestion.html')

###############################################################################
#
#       Objetivo:   Funcion para gestion de incidencias
#       Sustituye:  form_incidencias(request)
#                   modificar_incidencias(request):
#                   eliminar_incidencia(request):
#
##############################################################################

@csrf_exempt
def gestionar_incidencias(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        pak_id = request.POST.get('id')
        descripcion = request.POST.get('descripcion')
        empaque = Empaque.objects.get(id=request.POST.get('empaque'))
        producto = Producto.objects.get(id=request.POST.get('producto'))
        usuario = Usuario.objects.get(id=request.POST.get('usuario'))
        accion = request.POST.get('accion')

        if accion == 'Modificar':

            obj = Incidencia.objects.get(id=prod_id)
            obj.Descripcion = descripcion
            obj.Empaque = empaque
            obj.Producto = producto
            obj.Usuario = usuario
            obj.save()

            incidencias = {
                obj.id, obj.Descripcion, obj.Empaque,
                obj.Producto, obj.Usuario
                }
            return render (request, 'incidencias/lista_incidencia_modif.html', {'incidencias': incidencias})
        elif accion == "Borrar":
            incidencia = {
                obj.id, obj.Descripcion, obj.Empaque,
                obj.Producto, obj.Usuario
                }

            obj = Incidencia.objects.get(id=prod_id)
            obj.delete()

            return render (request, 'incidencias/lista_incidencia_modif.html', {'incidencia': incidencia})
        else:
            return render (request, 'incidencias/lista_incidencia_modif.html')

    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('incidencias/form_gestion.html')
        return HttpResponse(template.render())

###############################################################################
#
#       Objetivo:   Funcion para busqueda de incidencias
#
##############################################################################

@csrf_exempt
def form_buscar_incidencias(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        incidencias = Incidencia.objects.filter(Descripcion__contains=busqueda)
        return render (request, 'incidencias/lista_incidencias.html', {'incidencias': incidencias })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('incidencias/lista_incidencias.html')
        return HttpResponse(template.render())

###############################################################################
#
#       Obsoleto:   Funcion para gestion de incidencias
#
##############################################################################


"""
@csrf_exempt
def form_buscar_incidencias_eliminar(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        incidencias = Incidencia.objects.filter(Nombre__contains=busqueda)
        return render (request, 'incidencias/lista_incidencia_eliminar.html', {'incidencias': incidencias })
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('incidencias/lista_incidencias.html')
        return HttpResponse(template.render())
"""

@csrf_exempt
def form_incidencias(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        descripcion = request.POST.get('descripcion')
        empaque = Empaque.objects.get(id=request.POST.get('empaque'))
        producto = Producto.objects.get(id=request.POST.get('producto'))
        usuario = Usuario.objects.get(id=request.POST.get('usuario'))

        obj = Incidencia()
        obj.Descripcion = descripcion
        obj.Empaque = empaque
        obj.Producto = producto
        obj.Usuario = usuario
        obj.save()

        incidencias = Incidencia.objects.all()
        return render (request, 'incidencias/lista_incidencias.html', {'incidencias': incidencias})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('incidencias/form_gestion.html')
        return HttpResponse(template.render())

"""
@csrf_exempt
def modificar_incidencia(request):
    #if post request came
    if request.method == 'POST':
        #getting values from post
        pak_id = request.POST.get('id')
        descripcion = request.POST.get('descripcion')
        empaque = Empaque.objects.get(id=request.POST.get('empaque'))
        producto = Producto.objects.get(id=request.POST.get('producto'))
        usuario = Usuario.objects.get(id=request.POST.get('usuario'))

        obj = Incidencia.objects.get(id=prod_id)
        obj.Descripcion = descripcion
        obj.Empaque = empaque
        obj.Producto = producto
        obj.Usuario = usuario
        obj.save()

        incidencias = {
            obj.id, obj.Descripcion, obj.Empaque,
            obj.Producto, obj.Usuario
            }
        return render (request, 'incidencias/lista_incidencia_modif.html', {'incidencias': incidencias})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('incidencias/form_gestion.html')
        return HttpResponse(template.render())
"""
##############################################################################
#   Funcion para eliminacion de incidencias
#
"""
@csrf_exempt
def eliminar_incidencia(request):
    #if post request came

    if request.method == 'POST':
        #getting values from post
        pak_id = request.POST.get('id')
        descripcion = request.POST.get('descripcion')
        empaque = Empaque.objects.get(id=request.POST.get('empaque'))
        producto = Producto.objects.get(id=request.POST.get('producto'))
        usuario = Usuario.objects.get(id=request.POST.get('usuario'))

        incidencia = {
            obj.id, obj.Descripcion, obj.Empaque,
            obj.Producto, obj.Usuario
            }

        obj = Incidencia.objects.get(id=prod_id)
        obj.delete()

        return render (request, 'incidencias/lista_incidencia_modif.html', {'incidencia': incidencia})
    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('incidencias/form_gestion.html')
        return HttpResponse(template.render())
"""
