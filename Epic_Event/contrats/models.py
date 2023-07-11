from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

class Client(models.Model):

    NEW = 'NW'
    EXISTING = 'EX'

    CLIENT_TYPE = [
        (NEW, 'Sans contrats'),
        (EXISTING, 'Avec contrats'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL, null=True)
    client_type = models.CharField(max_length=2, choices=CLIENT_TYPE)

    def __str__(self):
        return f"Client n° : {self.id} - Company Name : {self.company_name}"

class Contrat(models.Model):

    #Permet d'enregistrer une date au format JJ/MM/AAAA
    date_regex = r'^\d{2}/\d{2}/\d{4}$'
    date_validator = RegexValidator(date_regex, 'Veuillez entrer une date au format JJ/MM/AAAA.')

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client,
                                       on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.CharField(max_length=10, validators=[date_validator])

    def __str__(self):
        return f"Contrat n° : {self.id} - Client : {self.client} " \
               f"- Création : {self.date_created} "
