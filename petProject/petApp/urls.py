from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/create/', views.pet_create, name='pet_create'),
    path('pets/page/<int:page_number>/', views.pet_list, name='pet_list_paginated'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('pets/<int:pet_id>/add-vaccination/', views.add_vaccination, name='add_vaccination'),
    path('pets/<int:pet_id>/delete-vaccination/<int:vaccination_id>/', views.delete_vaccination, name='delete_vaccination'),
    path('veterinaries/', views.veterinary_list, name='veterinary_list'),
    path('veterinaries/create/', views.veterinary_create, name='veterinary_create'),
    path('veterinaries/<pk>/', views.veterinary_detail, name='veterinary_detail'),
    path('pet-specialists/', views.pet_specialist_list, name='pet_specialist_list'),
    path('pet-specialists/create/', views.pet_specialist_create, name='pet_specialist_create'),
    path('pet-specialists/<pk>/', views.pet_specialist_detail, name='pet_specialist_detail'),
    path('vaccinations/', views.vaccination_list, name='vaccination_list'),
    path('vaccinations/create/', views.vaccination_create, name='vaccination_create'),
    path('vaccinations/<pk>/', views.vaccination_detail, name='vaccination_detail'),
    path('consultations/', views.consultation_list, name='consultation_list'),
    path('consultations/create/', views.consultation_create, name='consultation_create'),
    path('consultations/<pk>/', views.consultation_detail, name='consultation_detail'),
]