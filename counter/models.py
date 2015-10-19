from django.db import models

# Create your models here.

class Corporacion(models.Model):
	descripcion = models.CharField(max_length = 40)

	def __unicode__(self):
		return self.descripcion


class Partido(models.Model):
	descripcion = models.CharField(max_length = 60)
	abreviatura = models.CharField(max_length = 5)

	def __unicode__(self):
		return self.descripcion

class Localidad (models.Model):
	descripcion = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.descripcion

class TipoVoto(models.Model):
	descripcion = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.descripcion

class Candidato(models.Model):	
	nombre = models.CharField(max_length = 60)
	corporacion = models.ForeignKey(Corporacion)
	partido = models.ForeignKey(Partido)
	localidad = models.ForeignKey(Localidad)
	renglon =  models.SmallIntegerField()
	tipo_voto = models.ForeignKey(TipoVoto)
	documento = models.CharField(max_length = 15, unique = True)

	def __unicode__(self):
		return self.nombre

class Puesto(models.Model):
	descripcion = models.CharField(max_length = 30)
	mesas = models.SmallIntegerField()

	def __unicode__(self):
		return self.descripcion


class CORPORACION(object):
	JAL = '1'
	GOB = '2' 
	ALC = '3'
	CON = '4'
	ASA = '5' 

class VOTO(object):
	PREFERENTE = 3
	NO_APLICA = 2
	NO_PREFERENTE = 1

class E14(models.Model):
	puesto = models.ForeignKey(Puesto)
	mesa = models.SmallIntegerField()
	total_E11 = models.SmallIntegerField(help_text='Total sufragantes E11', null =True)
	total_urna = models.SmallIntegerField(help_text='Total Votos Urna', null =True)
	incinerados = models.SmallIntegerField(help_text='Total Votos Incinerados', null =True)
	votos_blancos = models.SmallIntegerField(null =True)
	votos_nulos = models.SmallIntegerField(null =True)
	votos_no_marcaros = models.SmallIntegerField(verbose_name='No marcados', null =True)
	observaciones = models.CharField(max_length = 300, null =True)

	def __unicode__(self):
		return "%s mesa %d" % (self.puesto.descripcion, self.mesa)

	class Meta:
		abstract = True


	@staticmethod
	def sincronize():

		puestos = Puesto.objects.all()
		corporaciones = [Gobernacion, Alcaldia, Asamblea, Concejo, JAL]
		for corporacion in corporaciones:
			for puesto in puestos:
				
				for mesa in range(1, int(puesto.mesas) +1):
					c = corporacion()
					c.puesto = puesto
					c.mesa = mesa
					c.save()

			#corporacion.sincronize()

class Votacion(models.Model):
 	votos = models.SmallIntegerField(null = True)

	def __unicode__(self):
		return "%s (%s)" % (self.candidato.nombre, self.candidato.partido.abreviatura)

	class Meta:
		abstract = True


class Gobernacion(E14):

	@staticmethod
	def sincronize():
		VotosGobernacion.sincronize()


	class Meta:
		verbose_name = "Gobernacion"
    	verbose_name_plural = "Gobernacion"	
    	ordering = ['puesto', 'mesa']




class VotosGobernacion(Votacion):
	candidato = models.ForeignKey(Candidato, limit_choices_to={'corporacion__id': CORPORACION.GOB } )
	gobernacion = models.ForeignKey(Gobernacion)

	@staticmethod
	def sincronize():
		mesas = Gobernacion.objects.all() 
		candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.GOB) 

		for mesa in mesas:
			
			for candidato in candidatos:
				row = VotosGobernacion()
				row.candidato = candidato
				row.gobernacion = mesa
				row.save()

	class Meta:
		ordering = ['candidato__partido', 'candidato__renglon',]

	

class Alcaldia(E14):
	
	@staticmethod
	def sincronize():
		VotosAlcaldia.sincronize()
	
	class Meta:
		verbose_name = "Alcaldia"
    	verbose_name_plural = "Alcaldia"
    	ordering = ['puesto', 'mesa']



	
class VotosAlcaldia(Votacion):
	candidato = models.ForeignKey(Candidato, limit_choices_to={'corporacion__id': CORPORACION.ALC } )
	alcaldia = models.ForeignKey(Alcaldia)

	@staticmethod
	def sincronize():
		mesas = Alcaldia.objects.all() 
		candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.ALC) 

		for mesa in mesas:
			for candidato in candidatos:
				row = VotosAlcaldia()
				row.candidato = candidato
				row.alcaldia = mesa
				row.save()

	class Meta:
		ordering = ['candidato__partido', 'candidato__renglon',]
		

class Asamblea(E14):
	
	@staticmethod
	def sincronize():
		VotosAsamblea.sincronize()
	
	class Meta:
		verbose_name = "Asamblea"
    	verbose_name_plural = "Asamblea"
    	ordering = ['puesto', 'mesa']


	

class VotosAsamblea(Votacion):
	candidato = models.ForeignKey(Candidato, limit_choices_to={'corporacion__id': CORPORACION.ASA } )
	asamblea = models.ForeignKey(Asamblea)

	@staticmethod
	def sincronize():
		mesas = Asamblea.objects.all() 
		candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.ASA).exclude(tipo_voto = VOTO.NO_PREFERENTE).order_by('partido')

		for mesa in mesas:

			for candidato in candidatos:

				row = VotosAsamblea()
				row.candidato = candidato
				row.asamblea = mesa
				row.save()

	def __unicode__(self):
		return "%s %s (%s)" % (self.candidato.renglon, self.candidato.nombre, self.candidato.partido.abreviatura)

	class Meta:
		ordering = ['candidato__partido', 'candidato__renglon',]
	

class Concejo(E14):

	@staticmethod
	def sincronize():
		VotosConcejo.sincronize()
	
	class Meta:
		verbose_name = "Concejo"
    	verbose_name_plural = "Concejo"
    	ordering = ['puesto', 'mesa']



	

class VotosConcejo(Votacion):
	candidato = models.ForeignKey(Candidato, limit_choices_to={'corporacion__id': CORPORACION.CON } )
	concejo = models.ForeignKey(Concejo)

	@staticmethod
	def sincronize():
		mesas = Concejo.objects.all() 
		for mesa in mesas:
			candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.CON).exclude(tipo_voto = VOTO.NO_PREFERENTE).order_by('partido')
			for candidato in candidatos:
				row = VotosConcejo()
				row.candidato = candidato
				row.concejo = mesa
				row.save()

	def __unicode__(self):
		return "%s %s (%s)" % (self.candidato.renglon, self.candidato.nombre, self.candidato.partido.abreviatura)

	class Meta:
		ordering = ['candidato__partido', 'candidato__renglon',]


class JAL(E14):

	@staticmethod
	def sincronize():
		VotosJAL.sincronize()
	
	class Meta:
		verbose_name = "JAL"
    	verbose_name_plural = "JAL"
    	ordering = ['puesto', 'mesa']



	

class VotosJAL(Votacion):
	candidato = models.ForeignKey(Candidato, limit_choices_to={'corporacion__id': CORPORACION.JAL } )
	jal = models.ForeignKey(JAL)

	@staticmethod
	def sincronize():
		mesas = JAL.objects.all() 
		for mesa in mesas:
			candidatos = Candidato.objects.filter(corporacion__id = CORPORACION.JAL, partido__id = 22).exclude(tipo_voto = VOTO.NO_PREFERENTE).order_by('partido')
			for candidato in candidatos:
				row = VotosJAL()
				row.candidato = candidato
				row.jal = mesa
				row.save()

	def __unicode__(self):
		return "%s %s (%s)" % (self.candidato.renglon, self.candidato.nombre, self.candidato.partido.abreviatura)

	class Meta:
		ordering = ['candidato__partido', 'candidato__renglon',]
