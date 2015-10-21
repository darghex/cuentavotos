from django.shortcuts import render, redirect 
from counter.models import * # Create your views here.
from django.db.models import Sum

def home(request):
	return redirect("/alcaldia")


def alcaldia(request):
	data = process(CORPORACION.ALC)
	return render(request, 'counter/index.html', data)

def gobernacion(request):
	data = process(CORPORACION.GOB)
	return render(request, 'counter/index.html', data)

def asamblea(request):
	data = process(CORPORACION.ASA)
	return render(request, 'counter/index.html', data)

def concejo(request):
	data = process(CORPORACION.CON)
	return render(request, 'counter/index.html', data)

def jal(request):
	data = process(CORPORACION.JAL)
	return render(request, 'counter/index.html', data)

def process(corporacion, zona = 1):
	candidatos = Candidato.objects.filter(corporacion__id = corporacion).order_by('partido') 
	zonas = Zona.objects.all()
	
	mesas = {'total': Puesto.objects.filter( zona__id = zona).aggregate(Sum('mesas'))['mesas__sum']}
	

	Model = None
	title = None
	if corporacion == CORPORACION.ALC:
		Model = Alcaldia
		title = 'Alcaldia'
	elif corporacion == CORPORACION.GOB:
		Model = Gobernacion
		title = 'Gobernacion'
	elif corporacion == CORPORACION.ASA:
		Model = Asamblea
		title = 'Asamblea'
	elif corporacion == CORPORACION.CON:
		Model = Concejo
		title = 'Concejo'
	elif corporacion == CORPORACION.JAL:
		Model = JAL
		title = 'JAL'

	mesas.update( {'reportadas': Model.objects.filter(puesto__zona__id = zona, total_E11__isnull = False).count() })
	mesas.update( {'noreportadas': Model.objects.filter(puesto__zona__id = zona, total_E11__isnull = True).count() })
	mesas.update( {'novedades': Model.objects.filter(puesto__zona__id = zona, observaciones__isnull = False).count() })

	return {'candidatos': candidatos, 'title': title, 'id': corporacion, 'zonas': zonas, 'mesas': mesas  }