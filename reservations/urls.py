from django.urls import path
from . import views
app_name = 'reservations'
urlpatterns = [
    path('', views.home, name='home'),
    path('creer_reservation/', views.creer_reservation, name='creer_reservation'),
    # URL pour gérer la redirection après la soumission réussie
    path('success/', views.success, name='success_url'),  
    # path('view/<int:candidat_id>/', views.view_reservations, name='view_reservations'),
    # path('evaluation/', views.submit_evaluation, name='submit_evaluation'),
    # path('reservation-success/', views.reservation_success, name='reservation_success'),
    # path('evaluation-success/', views.evaluation_success, name='evaluation_success'),
]