from django import template
from counter.models import *
register = template.Library()

@register.filter(name='votos')
def votos(obj, zona):
	cantidad = obj.votos(zona)
	if not cantidad:
		cantidad == 0
	return cantidad


def get_corporacion(corporacion):
	corp = None
	if corporacion == CORPORACION.ALC:
		corp = Alcaldia
	elif corporacion == CORPORACION.GOB:
		corp = Gobernacion
	elif corporacion == CORPORACION.ASA:
		corp == CORPORACION.ASA
	elif corporacion == CORPORACION.CON:
		corp == CORPORACION.CON
	elif corporacion == CORPORACION.JAL:
		corp == CORPORACION.JAL
	return corp

def votacion(tipo, corporacion, zona):
	corp = get_corporacion(corporacion)	
	cantidad = 0
	field = ''
	if tipo == 'b':
		field = 'votos_blancos'
	elif tipo == 'n':
		field = 'votos_nulos'
	elif tipo == 'm':
		field = 'votos_no_marcaros'
	elif tipo == 'i':
		field = 'incinerados'
	#if zona == -1:
	#	cantidad = corp.objects.all().aggregate(Sum(field))["%s__sum" % field]
	#else:
	#	cantidad = corp.objects.filter(puesto__zona__id = zona).aggregate(Sum(field))["%s__sum" % field]
	return cantidad


@register.filter(name='votos_blanco')
def votos_blanco(corporacion, zona):
	return votacion('b', corporacion, zona)

@register.filter(name='votos_nulos')
def votos_nulos(corporacion, zona):
	return votacion('n', corporacion, zona)

@register.filter(name='votos_no_marcados')
def votos_no_marcados(corporacion, zona):
	return votacion('m', corporacion, zona)

@register.filter(name='votos_incinerados')
def votos_incinerados(corporacion, zona):
	return votacion('i', corporacion, zona)