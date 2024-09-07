from django.contrib import admin
from .models import *

# Register your models here.

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('username', 'nom', 'prenom', 'email', 'phone', 'sexe', 'date_naissance')
    
class AvionAdmin(admin.ModelAdmin):
    list_display = ('type', 'nbre_place', 'nom', 'date_creation')
    
class CompagnieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'date_creation')
    
class AeroportAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'telephone', 'date_creation')
    
class VolAdmin(admin.ModelAdmin):
    list_display = ('avion', 'compagnie', 'aeroport_depart', 'aeroport_arrive', 'heure_depart', 'heure_arrive', 'date_creation')
    
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'vol', 'date_creation')
    
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Avion, AvionAdmin)
admin.site.register(Compagnie, CompagnieAdmin)
admin.site.register(Aeroport, AeroportAdmin)
admin.site.register(Vol, VolAdmin)
admin.site.register(Reservation, ReservationAdmin)

admin.sites.AdminSite.site_header = 'RESERVATION DE VOLS EN LIGNE'
admin.sites.AdminSite.site_title = 'RESERVATION DE VOLS EN LIGNE'
    