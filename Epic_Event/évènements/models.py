from django.db import models
from django.conf import settings
from contrats.models import Contrat
from django.core.validators import RegexValidator



class Event(models.Model):

    #Permet d'enregistrer une date au format JJ/MM/AAAA
    date_regex = r'^\d{2}/\d{2}/\d{4}$'
    date_validator = RegexValidator(date_regex, 'Veuillez entrer une date au format JJ/MM/AAAA.')

    PREPARATION = 'PR'
    IN_PROGRESS = 'IP'
    FINISHED = 'FN'

    EVENT_STATUS = [
        (PREPARATION, 'En preparation'),
        (IN_PROGRESS, 'En cours'),
        (FINISHED, 'Terminé'),
    ]

    contrat = models.OneToOneField(Contrat,
                                       on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL, null=True,
                                        limit_choices_to={'user_profile': 'SU'})
    event_status = models.CharField(max_length=2, choices=EVENT_STATUS)
    attendees = models.IntegerField()
    event_date = models.CharField(max_length=10, validators=[date_validator])
    notes = models.TextField(blank=True)

    def get_event_status_display(self):
        return dict(Event.EVENT_STATUS)[self.event_status]

    def __str__(self):
        return f"Evènement n° : {self.id} - Date : {self.event_date} " \
               f"- Status : {self.get_event_status_display()} "
