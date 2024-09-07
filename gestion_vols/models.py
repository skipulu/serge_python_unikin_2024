from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username and password.
        """
        if not username:
            raise ValueError(_("The username must be set"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given username and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, password, **extra_fields)



class Utilisateur(AbstractBaseUser, PermissionsMixin):
    SEXE_CHOICE =(
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    username = models.CharField(_("username"), unique=True, max_length=50)
    nom = models.CharField(max_length=50, null=True, blank=True)
    prenom = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    sexe=models.CharField(choices=SEXE_CHOICE, max_length=50,null=True)
    date_naissance=models.DateField(null=True)
    lieu_naissance=models.CharField(max_length=50,null=True)
    ville=models.CharField(max_length=50,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now) 

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
      verbose_name = "user"

    def __str__(self):
        return f"{self.username}"
    

class Avion(models.Model):
    type=models.CharField(max_length=50,null=True)
    nbre_place=models.IntegerField()
    nom=models.CharField(max_length=50,null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nom}"

class Compagnie(models.Model):
    nom=models.CharField(max_length=50,null=True)
    description=models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nom}"

class Aeroport(models.Model):
    nom=models.CharField(max_length=50,null=True)
    ville=models.CharField(max_length=50,null=True)
    telephone=models.CharField(max_length=50,null=True)
    description=models.TextField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nom}"

class Vol(models.Model):
    avion=models.ForeignKey(Avion, on_delete=models.CASCADE)
    compagnie=models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    aeroport_depart=models.ForeignKey(Aeroport, on_delete=models.CASCADE)
    heure_depart=models.DateTimeField()
    aeroport_arrive=models.ForeignKey(Aeroport,related_name='Aeroport', on_delete=models.CASCADE)
    heure_arrive=models.DateTimeField()
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.avion} {self.aeroport_depart} {self.aeroport_arrive}"
  

class Reservation(models.Model):
    utilisateur=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    vol=models.ForeignKey(Vol, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.utilisateur} {self.vol}"
  