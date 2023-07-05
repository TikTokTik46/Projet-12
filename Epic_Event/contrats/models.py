from django.db import models
from django.conf import settings

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
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL, null=True)
    client_type = models.CharField(max_length=2, choices=CLIENT_TYPE)

    def __str__(self):
        return f"Client n° : {self.id} - Company Name : {self.company_name}"

class Contrat(models.Model):
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client,
                                       on_delete=models.SET_NULL, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateField()

    def __str__(self):
        return f"Contrat n° : {self.id} - Client : {self.client} " \
               f"- Création : {self.date_created} "
