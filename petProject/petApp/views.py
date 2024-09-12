from django.shortcuts import render, redirect
from .models import Pet, Veterinary, PetSpecialist, Vaccination, Consultation, PetVaccination
from .forms import PetForm, VeterinaryForm, PetSpecialistForm, VaccinationForm, ConsultationForm, AddVaccinationForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
def home(request):
    return render(request, 'home.html')

@login_required
def pet_list(request):
    query = request.GET.get('q')
    if query:

        pets = Pet.objects.filter(name__icontains=query)

    else:

        pets = Pet.objects.all()
    paginator = Paginator(pets, 15)  # 25 values per page

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'pet_list.html', {'page_obj': page_obj, 'query': query})
@login_required
def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pet_form.html', {'form': form})
@login_required
def pet_detail(request, **kwargs):
    pet_id = kwargs.get('pet_id')
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'pet_detail.html', {'pet': pet})
@login_required
def veterinary_list(request):
    query = request.GET.get('q')
    if query:
        veterinaries = Veterinary.objects.filter(name__icontains=query)
    else:
        veterinaries = Veterinary.objects.all()
    paginator = Paginator(veterinaries, 15)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'veterinary_list.html', {'page_obj': page_obj, 'query': query})
@login_required
def veterinary_create(request):
    if request.method == 'POST':
        form = VeterinaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veterinary_list')
    else:
        form = VeterinaryForm()
    return render(request, 'veterinary_form.html', {'form': form})
@login_required
def veterinary_detail(request, pk):
    veterinary = Veterinary.objects.get(pk=pk)
    return render(request, 'veterinary_detail.html', {'veterinary': veterinary})

@login_required
def pet_specialist_list(request):
    query = request.GET.get('q')
    if query:
        pet_specialists = PetSpecialist.objects.filter(name__icontains=query)
    else:
        pet_specialists = PetSpecialist.objects.all()
    paginator = Paginator(pet_specialists, 15) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pet_specialist_list.html', {'page_obj': page_obj, 'query': query})
@login_required
def pet_specialist_create(request):
    if request.method == 'POST':
        form = PetSpecialistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_specialist_list')
    else:
        form = PetSpecialistForm()
    return render(request, 'pet_specialist_form.html', {'form': form})
@login_required
def pet_specialist_detail(request, pk):
    pet_specialist = PetSpecialist.objects.get(pk=pk)
    return render(request, 'pet_specialist_detail.html', {'pet_specialist': pet_specialist})
@login_required
def vaccination_list(request):
    query = request.GET.get('q')
    if query:
        vaccinations = Vaccination.objects.filter(name__icontains=query)
    else:
        vaccinations = Vaccination.objects.all()
    paginator = Paginator(vaccinations, 15)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vaccination_list.html', {'page_obj': page_obj, 'query': query})
@login_required
def vaccination_create(request):
    if request.method == 'POST':
        form = VaccinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccination_list')
    else:
        form = VaccinationForm()
    return render(request, 'vaccination_form.html', {'form': form})
@login_required
def vaccination_detail(request, pk):
    vaccination = Vaccination.objects.get(pk=pk)
    return render(request, 'vaccination_detail.html', {'vaccination': vaccination})
@login_required
def consultation_list(request):
    query = request.GET.get('q')
    if query:
        consultations = Consultation.objects.filter(pet__name__icontains=query)
    else:
        consultations = Consultation.objects.all()
    paginator = Paginator(consultations, 15)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'consultation_list.html', {'page_obj': page_obj, 'query': query})
@login_required
def consultation_create(request):
    pets = Pet.objects.all()
    veterinarians = Veterinary.objects.all()
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultation_list')
    else:
        form = ConsultationForm()

    return render(request, 'consultation_form.html', {'form': form, 'pets': pets, 'veterinarians': veterinarians})
@login_required
def consultation_detail(request, pk):
    consultation = Consultation.objects.get(pk=pk)
    return render(request, 'consultation_detail.html', {'consultation': consultation})

@login_required
def add_vaccination(request, pet_id):
    pet = Pet.objects.get(id=pet_id)

    if request.method == 'POST':
        form = AddVaccinationForm(request.POST)

        if form.is_valid():
            vaccination = form.cleaned_data['vaccination']

            if PetVaccination.objects.filter(pet=pet, vaccination=vaccination).exists():
                form.add_error(None, 'Vaccination already added for this pet!')
            else:
                pet_vaccination = form.save(commit=False)
                pet_vaccination.pet = pet
                pet_vaccination.save()
                return redirect('pet_detail', pet_id=pet_id)

    else:
        form = AddVaccinationForm()

    return render(request, 'add_vaccination.html', {'form': form, 'pet': pet})

@login_required
def delete_vaccination(request, pet_id, vaccination_id):

    pet = Pet.objects.get(id=pet_id)

    vaccination = Vaccination.objects.get(id=vaccination_id)

    pet_vaccination = PetVaccination.objects.get(pet=pet.id, vaccination=vaccination)

    pet_vaccination.delete()

    return redirect('pet_detail', pet_id=pet_id)