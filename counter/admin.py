from django.contrib import admin

# Register your models here.
from counter.models import *
from django import forms
"""
@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    pass


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    pass
"""

class VotosAdmin(admin.TabularInline):
	verbose_name = "Voto"
	verbose_name_plural = "Votos"
	extra = 0
	readonly_fields = ('candidato',)
	fields = ('votos',)
	
	def has_add_permission(self, request, obj=None):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

class E14Form( forms.ModelForm ):
    observaciones = forms.CharField( widget=forms.Textarea )    
    
    class Meta:
        model = E14
        fields = '__all__'


class CorporacionAdmin(admin.ModelAdmin):
	
    search_fields = ('puesto__descripcion', 'mesa')
    list_filter = ('puesto',)
    readonly_fields = ('puesto', 'mesa')
    fieldsets = [
        (None, {'fields': [ ('puesto','mesa'),'total_E11', 
        'total_urna', 'incinerados','votos_blancos', 'votos_nulos', 'votos_no_marcaros','observaciones'

        ]}), ]  
    form = E14Form


class VotosGobernacionAdmin(VotosAdmin):
    model = VotosGobernacion
    
@admin.register(Gobernacion)
class GobernacionAdmin(CorporacionAdmin):
	inlines = [VotosGobernacionAdmin,]

class VotosAlcaldiaAdmin(VotosAdmin):
    model = VotosAlcaldia
    
@admin.register(Alcaldia)
class AlcaldiaAdmin(CorporacionAdmin):
	inlines = [VotosAlcaldiaAdmin,]

class VotosAsambleaAdmin(VotosAdmin):
    model = VotosAsamblea
    
@admin.register(Asamblea)
class AsambleaAdmin(CorporacionAdmin):
	inlines = [VotosAsambleaAdmin,]
    
class VotosConcejoAdmin(VotosAdmin):
    model = VotosConcejo
    
@admin.register(Concejo)
class ConcejoAdmin(CorporacionAdmin):
	inlines = [VotosConcejoAdmin,]

class VotosJALAdmin(VotosAdmin):
    model = VotosJAL
    
@admin.register(JAL)
class JALAdmin(CorporacionAdmin):
	inlines = [VotosJALAdmin,]


admin.site.disable_action('delete_selected')