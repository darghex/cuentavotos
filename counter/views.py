from django.shortcuts import render, redirect 
from counter.models import * # Create your views here.
from django.db.models import Sum

def home(request):
	return redirect("/alcaldia")

def alcaldia(request):
	data = process(CORPORACION.ALC, getZone(request.POST))
	return render(request, 'counter/index.html', data)

def gobernacion(request):
	data = process(CORPORACION.GOB, getZone(request.POST))
	return render(request, 'counter/index.html', data)

def asamblea(request):
	data = process(CORPORACION.ASA, getZone(request.POST))
	return render(request, 'counter/index.html', data)

def concejo(request):
	data = process(CORPORACION.CON, getZone(request.POST))
	return render(request, 'counter/index.html', data)

def jal(request):
	data = process(CORPORACION.JAL, getZone(request.POST))
	return render(request, 'counter/index.html', data)

def observaciones(request):
	data = ""
	zona = "Todas"
	if request.GET['zona'] != u'-1':
		data = Alcaldia.objects.filter(puesto__zona__id = request.GET['zona'], observaciones__isnull = False)		
		zona = Zona.objects.get(pk = request.GET['zona']).numero
	else:
		data = Alcaldia.objects.filter(observaciones__isnull = False)		

	return render(request, 'counter/detalle.html', {'observaciones': data, 'zona': zona})

def process(corporacion, zona = -1):
	candidatos = Candidato.objects.filter(corporacion__id = corporacion).order_by('partido','renglon') 
	zonas = Zona.objects.all()
	
	if zona == -1:
		mesas = {'total': Puesto.objects.all().aggregate(Sum('mesas'))['mesas__sum']}

	else:
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

	if zona == -1:
		mesas.update( {'reportadas': Model.objects.filter(total_E11__isnull = False).count() })
		mesas.update( {'noreportadas': Model.objects.filter(total_E11__isnull = True).count() })
		mesas.update( {'novedades': Model.objects.filter( observaciones__isnull = False).count() })
	else:
		mesas.update( {'reportadas': Model.objects.filter(puesto__zona__id = zona, total_E11__isnull = False).count() })
		mesas.update( {'noreportadas': Model.objects.filter(puesto__zona__id = zona, total_E11__isnull = True).count() })
		mesas.update( {'novedades': Model.objects.filter(puesto__zona__id = zona, observaciones__isnull = False).count() })

	return {'candidatos': candidatos, 'title': title, 'id': corporacion, 'zonas': zonas, 'zona_id': zona, 'mesas': mesas  }

def getZone(POST):
	if POST.has_key('selectZona'):
		return int(POST['selectZona'])
	else:
		return -1