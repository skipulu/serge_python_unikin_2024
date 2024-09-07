from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q

# Create your views here.
def page_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('vols')
    return render(request, 'authentication-login.html')

def page_register(request):
    message = ""
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = Utilisateur(
                nom = request.POST.get('nom'),
                prenom = request.POST.get('prenom'),
                email = request.POST.get('email'),
                username = request.POST.get('email'),
            )
            user.password = user.set_password(password1)
            user.save()
            message = "Success"
            login(request, user)
            return redirect('vols')
        else:
            message = "Mot de passe différents"
    return render(request, 'authentication-register.html', {"message":message})

def page_list_vols(request):
    list_aeroports = Aeroport.objects.all()
    list_vols = Vol.objects.all()
    aer_depart = request.GET.get('aer_depart')
    aer_arrivee = request.GET.get('aer_arrivee')
    if aer_depart and aer_arrivee:
        list_vols.filter(aeroport_depart__id=aer_depart, aeroport_arrive__id=aer_arrivee)
    return render(request, 'index.html', {"list_aeroports":list_aeroports, "list_vols":list_vols})

def reserver(request):  
    vol = Vol.objects.get(pk = request.GET.get('pk'))
    Reservation.objects.get_or_create(
        vol = vol,
        utilisateur = request.user
    )
    return redirect(f"{reverse('vols')}?message=Réservation réussi")



