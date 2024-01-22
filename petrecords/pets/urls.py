from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.pet_list, name='pet_list'),
    path('<int:pet_id>/services/', views.vet_service_list, name='vet_service_list'),
    # Dodajte URL-ove prema potrebi
]