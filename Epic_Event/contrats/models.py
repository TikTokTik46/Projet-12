from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

class Client(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL, null=True,
                                      limit_choices_to={'user_profile': 'SA'})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Contrat(models.Model):

    SIGNE = 'SI'
    DEVIS_A_REALISER = 'DR'
    DEVIS_ENVOYE = 'DE'

    CONTRAT_STATUS = [
        (SIGNE, 'Signé'),
        (DEVIS_A_REALISER, 'Devis a réaliser'),
        (DEVIS_ENVOYE, 'Devis envoyé'),
    ]


    #Permet d'enregistrer une date au format JJ/MM/AAAA
    date_regex = r'^\d{2}/\d{2}/\d{4}$'
    date_validator = RegexValidator(date_regex, 'Veuillez entrer une date au format JJ/MM/AAAA.')

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL, null=True,
                                      limit_choices_to={'user_profile': 'SA'})
    client = models.ForeignKey(Client,
                                       on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=CONTRAT_STATUS, default='DR')
    amount_in_euros = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    payment_due = models.CharField(max_length=10, validators=[date_validator], null=True)

    def __str__(self):
        return f"Contrat n° : {self.id} - Client : {self.client} " \
               f"- Création : {self.date_created} "
