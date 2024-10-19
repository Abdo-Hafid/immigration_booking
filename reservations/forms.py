from django import forms
from .models import FormulaireEvaluation,Reservation,Candidat

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = FormulaireEvaluation
        fields = ['prenom', 'name', 'email', 'adresse', 'ville', 'num', 'niveau_diplome', 
                  'domaine_formation', 'date_obtention', 'niveau_francais', 'niveau_anglais', 
                  'duree_experience', 'disponibilite']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'service']

class CandidatForm(forms.ModelForm):
    model = Candidat
    fields = ['prenom', 'name', 'email', 'num', 'adresse', 'ville']
    def __str__(self):
        return self.name