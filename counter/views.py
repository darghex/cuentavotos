from django.shortcuts import render, redirect 
from counter.models import * # Create your views here.
from django.db.models import Sum

def home(request):
	return redirect("/alcaldia")

def alcaldia(request):
	data = process(CORPORACION.ALC, getZone(request.POST) , getPuesto(request.POST))
	return render(request, 'counter/index.html', data)

def gobernacion(request):
	data = process(CORPORACION.GOB, getZone(request.POST), getPuesto(request.POST))
	return render(request, 'counter/index.html', data)

def asamblea(request):
	data = process(CORPORACION.ASA, getZone(request.POST), getPuesto(request.POST))
	return render(request, 'counter/index.html', data)

def concejo(request):
	data = process(CORPORACION.CON, getZone(request.POST), getPuesto(request.POST))
	return render(request, 'counter/index.html', data)

def jal(request):
	data = process(CORPORACION.JAL, getZone(request.POST), getPuesto(request.POST))
	return render(request, 'counter/index.html', data)

def observaciones(request):
	data = ""
	zona = "Todas"
	puesto = "Todos"
	
	if request.GET['zona'] != u'-1':
		if request.GET['puesto'] == u'-1':
			data = Alcaldia.objects.filter(puesto__zona__id = request.GET['zona'], observaciones__isnull = False)		
		else:
			data = Alcaldia.objects.filter(puesto__zona__id = request.GET['zona'], puesto__id = request.GET['puesto'], observaciones__isnull = False)		
			puesto = Puesto.objects.get(pk = request.GET['puesto']).descripcion

		zona = Zona.objects.get(pk = request.GET['zona']).numero
	else:
		if request.GET['puesto'] == u'-1':
			data = Alcaldia.objects.filter(observaciones__isnull = False)		
		else:
			data = Alcaldia.objects.filter(observaciones__isnull = False, puesto__id = request.GET['puesto'])		
			puesto = Puesto.objects.get(pk = request.GET['puesto']).descripcion



	return render(request, 'counter/detalle.html', {'observaciones': data, 'zona': zona, 'puesto': puesto})

def process(corporacion, zona = -1, puesto = -1):
	candidatos = Candidato.objects.filter(corporacion__id = corporacion).exclude(tipo_voto = VOTO.NO_PREFERENTE).order_by('partido','renglon') 
	zonas = Zona.objects.all()
	puestos = None
	if zona == -1:
		puestos = Puesto.objects.all()
	else:
		puestos = Puesto.objects.filter(zona__id = zona)

	if zona == -1:
		if puesto == -1:
			mesas = {'total': Puesto.objects.all().aggregate(Sum('mesas'))['mesas__sum']}
		else:
			mesas = {'total': Puesto.objects.filter(id = puesto).aggregate(Sum('mesas'))['mesas__sum']}
	else:
		if puesto == -1:
			mesas = {'total': Puesto.objects.filter( zona__id = zona).aggregate(Sum('mesas'))['mesas__sum']}		
		else:
			mesas = {'total': Puesto.objects.filter( zona__id = zona, id = puesto).aggregate(Sum('mesas'))['mesas__sum']}		
	
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
		if puesto == -1:
			mesas.update( {'reportadas': Model.objects.filter(total_E11__isnull = False).count() })
			mesas.update( {'noreportadas': Model.objects.filter(total_E11__isnull = True).count() })
			mesas.update( {'novedades': Model.objects.filter( observaciones__isnull = False).count() })
		else:
			mesas.update( {'reportadas': Model.objects.filter(total_E11__isnull = False, puesto__id = puesto).count() })
			mesas.update( {'noreportadas': Model.objects.filter(total_E11__isnull = True, puesto__id = puesto).count() })
			mesas.update( {'novedades': Model.objects.filter( observaciones__isnull = False, puesto__id = puesto).count() })

	else:
		if puesto == -1:
			mesas.update( {'reportadas': Model.objects.filter(puesto__zona__id = zona, total_E11__isnull = False).count() })
			mesas.update( {'noreportadas': Model.objects.filter(puesto__zona__id = zona, total_E11__isnull = True).count() })
			mesas.update( {'novedades': Model.objects.filter(puesto__zona__id = zona, observaciones__isnull = False).count() })
		else:
			mesas.update( {'reportadas': Model.objects.filter(puesto__zona__id = zona, puesto__id = puesto, total_E11__isnull = False).count() })
			mesas.update( {'noreportadas': Model.objects.filter(puesto__zona__id = zona, puesto__id = puesto, total_E11__isnull = True).count() })
			mesas.update( {'novedades': Model.objects.filter(puesto__zona__id = zona, puesto__id =puesto, observaciones__isnull = False).count() })
				
	
	des_zona = "Todas"
	if zona != -1:
		des_zona  = Zona.objects.get(id = zona).numero

	des_puesto = "Todos"
	if puesto != -1:
		des_puesto  = Puesto.objects.get(id = puesto).descripcion

	return {'candidatos': candidatos, 'title': title, 'id': corporacion, 'zonas': zonas, 'zona_id': zona, 'puesto_id': puesto, 'd_zona': des_zona, 'd_puesto': des_puesto, 'mesas': mesas, 'puestos': puestos  }

def getZone(POST):
	if POST.has_key('selectZona'):
		return int(POST['selectZona'])
	else:
		return -1

def getPuesto(POST):

	if POST.has_key('selectPuesto'):
		return int(POST['selectPuesto'])
	else:
		return -1