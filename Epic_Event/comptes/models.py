from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    GESTION = 'GE'
    SALE = 'SA'
    SUPPORT = 'SU'

    USER_PROFILES = [
        (GESTION, 'Gestion'),
        (SALE, 'Vente'),
        (SUPPORT, 'Support'),
    ]

    user_profile = models.CharField(max_length=2, choices=USER_PROFILES)

