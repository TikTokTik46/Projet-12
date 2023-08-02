from django.contrib.auth.models import AbstractUser, Permission
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

    def get_user_profile_display(self):
        profile_dict = dict(self.USER_PROFILES)
        return profile_dict.get(self.user_profile, self.user_profile)

    def __str__(self):
        return f"{self.email} - {self.id} - {self.get_user_profile_display()}"

    def save(self, *args, **kwargs):
        if self.user_profile == User.GESTION:
            self.is_staff = True
            self.is_superuser = True
        super().save(*args, **kwargs)