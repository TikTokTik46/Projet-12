from django.db import models
from django.conf import settings
from contrats.models import Contrat


class Event(models.Model):

    PREPARATION = 'PR'
    IN_PROGRESS = 'IP'
    FINISHED = 'FN'

    EVENT_STATUS = [
        (PREPARATION, 'En preparation'),
        (IN_PROGRESS, 'En cours'),
        (FINISHED, 'Terminé'),
    ]

    contrat = models.OneToOneField(Contrat,
                                       on_delete=models.SET_NULL, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL, null=True)
    event_status = models.CharField(max_length=2, choices=EVENT_STATUS)
    attendees = models.IntegerField()
    event_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Evènement n° : {self.id} - Client : {self.client} " \
               f"- Création : {self.date_created} "
