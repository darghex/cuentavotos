from django.shortcuts import render, redirect
from counter.models import *
# Create your views here.


def home(request):
	return redirect("/alcaldia")


def alcaldia(request):
	candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.ALC).order_by('partido') 
	return render(request, 'counter/index.html', {'candidatos': candidatos, 'title': 'Alcaldia', 'id': CORPORACION.ALC  })

def gobernacion(request):
	candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.GOB).order_by('partido') 
	return render(request, 'counter/index.html', {'candidatos': candidatos, 'title': 'Gobernacion', 'id': CORPORACION.GOB })

def asamblea(request):
	candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.ASA).exclude(tipo_voto = VOTO.NO_PREFERENTE).order_by('partido','renglon') 
	return render(request, 'counter/index.html', {'candidatos': candidatos, 'title': 'Asamblea', 'id': CORPORACION.ASA })

def concejo(request):
	candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.CON).exclude(tipo_voto = VOTO.NO_PREFERENTE).order_by('partido', 'renglon') 
	return render(request, 'counter/index.html', {'candidatos': candidatos, 'title': 'Concejo', 'id': CORPORACION.CON })

def jal(request):
	candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.JAL).exclude(tipo_voto = VOTO.NO_PREFERENTE).order_by('partido','renglon') 
	return render(request, 'counter/index.html', {'candidatos': candidatos, 'title': 'JAL', 'id': CORPORACION.JAL })