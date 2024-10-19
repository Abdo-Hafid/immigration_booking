from django.contrib import admin
from .models import Reservation, Candidat
# Register your models here.
@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'name', 'email', 'ville', 'num')  # Affiche ces champs dans la liste admin
    search_fields = ('prenom', 'name', 'email', 'ville')  # Champs de recherche
    list_filter = ('ville',)  # Filtres pour faciliter la gestion

# Enregistrement du modèle Reservation
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('candidat', 'date', 'time', 'service', 'status')  # Champs affichés dans l'admin
    search_fields = ('candidat__name', 'date', 'service')  # Recherche par nom de candidat, date et service
    list_filter = ('status', 'service')  # Filtres pour le statut et le service
    date_hierarchy = 'date'  # Filtre chronologique pour les réservations