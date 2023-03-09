from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse 
from .models import pregunta, Eleccion

# Create your views here.
def index(request):
    #Consulta la DB ORM
    # SQL : Select * from pregunta orden by desc fecha pub limit 5
    ultimas_preguntas=pregunta.objects.order_by('-fecha_pub')[:10]

    template=loader.get_template('polls/index.html')
    contexto={
        'ultimas_preguntas':ultimas_preguntas
    }
    return HttpResponse(template.render(contexto, request))

def holamanuel(request):
    return HttpResponse("<h1> HOLA MANUEL </h1>")

def detalle(request,id_pregunta):
    try:
        #Select * from * pregunta where id=id_pregunta
        pre=pregunta.objects.get(pk=id_pregunta)
        template=loader.get_template('polls/detalle.html')
        contexto={
            'pregunta':pre
         }
        return HttpResponse(template.render(contexto, request))
    except pregunta.DoesNotExist:
        raise Http404("La pregunta no existe")

def resultados(request,id_pregunta):
    pre=get_object_or_404(pregunta, pk=id_pregunta)
    template=loader.get_template('polls/resultados.html')
    contexto = {
        'pregunta':pre
    }
    return HttpResponse(template.render(contexto, request))

def votar(request,id_pregunta):
    pre=get_object_or_404(pregunta, pk=id_pregunta)
    try:
         opcion_seleccionada=Eleccion.objects.get(pk=request.POST["elegir"])
    except (KeyError, Eleccion.DoesNotExist):
        template_detalle=loader.get_template("polls/detalle.html")
        contexto = {
            'pregunta':pre,
            'mensaje_error': "La opción que elegiste no existe... "
        }  
        return HttpResponse(template_detalle.render(contexto, request))
    else:
        opcion_seleccionada.votos += 1
        opcion_seleccionada.save()
        return HttpResponseRedirect(reverse('polls:resultados', args=(pre.id, ) ))
   