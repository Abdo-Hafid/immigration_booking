from django.db import models

class Reservation(models.Model):
    candidat = models.ForeignKey('Candidat', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=25, choices=[
        ('à distance', 'À distance'),
        ('En personne', 'En personne'),
    ], default='En personne')
    status = models.CharField(max_length=20, choices=[
        ('pending', 'En attente'),
        ('confirmed', 'Confirmé'),
        ('canceled', 'Annulé')
    ], default='pending')

    def __str__(self):
        return f"{self.candidat.name} - {self.date} {self.time}"

class Candidat(models.Model):
    prenom = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    num = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class FormulaireEvaluation(models.Model):
    prenom = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    num = models.CharField(max_length=15)

    NIVEAU_DIPLOME_CHOICES = [
        ('Baccalauréat', 'Baccalauréat'),
        ('Licence', 'Licence'),
        ('Master', 'Master'),
        ('Doctorat', 'Doctorat'),
    ]
    niveau_diplome = models.CharField(max_length=50, choices=NIVEAU_DIPLOME_CHOICES)

    domaine_formation = models.CharField(max_length=100)
    date_obtention = models.DateField()

    NIVEAU_LANGUE_CHOICES = [
        ('Débutant', 'Débutant'),
        ('Intermédiaire', 'Intermédiaire'),
        ('Avancé', 'Avancé'),
        ('Courant', 'Courant'),
    ]
    niveau_francais = models.CharField(max_length=20, choices=NIVEAU_LANGUE_CHOICES)
    niveau_anglais = models.CharField(max_length=20, choices=NIVEAU_LANGUE_CHOICES)

    duree_experience = models.IntegerField(help_text="Durée en années")

    disponibilite = models.BooleanField(help_text="Êtes-vous disponible immédiatement ?")

    def __str__(self):
        return f"{self.name} - {self.niveau_diplome} ({self.domaine_formation})"
