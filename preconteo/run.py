def ciudad(row):
    return row['municipio'] == u'ESPINAL'    

def jal( row):
    return  row['corporacion'] == 'JUNTA ADMINISTRADORA LOCAL'

def alcaldia( row):
    return  row['corporacion'] == 'ALCALDIAS MUNICIPALES'

def concejo(row):
    return row['corporacion'] == 'CONCEJO MUNICIPAL'

def asamblea(row):
    return row['departamento'] == u'TOLIMA' and row['corporacion'] == 'ASAMBLEA DEPARTAMENTAL'

def gobernacion(row):
    return row['departamento'] == u'TOLIMA' and row['corporacion'] == 'GOBERNACION DEPARTAMENTAL'
    
from counter.models import *

def start():
	
	import json
	import os
	from preconteo.settings import BASE_DIR
	from heapq import merge
	from counter.models import VOTO, E14

	f = os.path.join(BASE_DIR, 'app_.json')
	file = open(f).read()
	data = json.loads(file)
	 
	listas = list( merge(filter(ciudad, data),filter(gobernacion, data), filter(asamblea, data) )) 
	
	for i,row in enumerate(listas):
		print row
		try:
			c = Corporacion.objects.get(descripcion  = row['corporacion'])
		except Corporacion.DoesNotExist:
			c = Corporacion(descripcion = row['corporacion'])
			c.save()

		try:
			l = Localidad.objects.get(descripcion  = row['localidad'])
		except Localidad.DoesNotExist:
			l = Localidad(descripcion = row['localidad'])
			l.save()

		try:
			t = TipoVoto.objects.get(descripcion  = row['tipo_voto'])
		except TipoVoto.DoesNotExist:
			t = TipoVoto(descripcion = row['tipo_voto'])
			t.save()

		try:
			p = Partido.objects.get(descripcion  = row['partido_grupo'])
		except Partido.DoesNotExist:
			p = Partido(descripcion = row['partido_grupo'])
			p.save()

			candidato = Candidato()
			candidato.nombre = row['partido_grupo']
			candidato.partido = p
			candidato.localidad_id = 2
			candidato.renglon = 0
			candidato.tipo_voto_id = VOTO.NO_APLICA
			candidato.corporacion = c
			candidato.documento = i
			try:
				candidato.save()
			except:
				pass


		

		candidato = Candidato()
		candidato.nombre = row['nombre_candidato']
		candidato.partido = p
		candidato.localidad = l
		candidato.renglon = row['renglon']
		candidato.tipo_voto = t
		candidato.corporacion = c
		candidato.documento = row['cedula']
		try:
			candidato.save()
		except:
			pass

	print "Datos Cargados"