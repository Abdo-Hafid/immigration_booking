from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Candidat
from .forms import ReservationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Candidat
from .forms import ReservationForm
from django.urls import reverse

def home(request):
    return render(request, 'index.html')
def success(request):
    return render(request, 'success.html')

# def make_reservation(request, candidat_id):
#     candidat = get_object_or_404(Candidat, id=candidat_id)
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             reservation = form.save(commit=False)
#             reservation.candidat = candidat
#             reservation.save()
#             return redirect('reservation_success')
#     else:
#         form = ReservationForm()
#     return render(request, 'reservations/make_reservation.html', {'form': form, 'candidat': candidat})

def creer_reservation(request):
    if request.method == 'POST':
        # Récupérer les informations du candidat
        prenom = request.POST.get('prenom')
        name = request.POST.get('name')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        num = request.POST.get('num')

        # Validation simple des données
        if not prenom or not name or not email:
            messages.error(request, 'Veuillez remplir tous les champs obligatoires.')
            return redirect('reservations:index')  # Redirige vers la page de réservation

        # Créer ou récupérer le candidat
        candidat, created = Candidat.objects.get_or_create(
            prenom=prenom,
            name=name,
            email=email,
            adresse=adresse,
            ville=ville,
            num=num
        )

        # Récupérer les informations de la réservation
        date = request.POST.get('date')
        time = request.POST.get('time')
        service = request.POST.get('service')

        # Créer la réservation
        try:
            Reservation.objects.create(
                candidat=candidat,
                date=date,
                time=time,
                service=service,
                status='pending',
            )
            messages.success(request, 'Réservation créée avec succès !')
        except Exception as e:
            messages.error(request, 'Erreur lors de la création de la réservation : {}'.format(e))
            return redirect('reservations:index')  # Redirige vers la page de réservation

        return redirect('reservations:success_url')  # Redirige après la soumission réussie

    return render(request, 'index.html')
