# Generated by Django 4.2.2 on 2023-07-17 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('évènements', '0007_alter_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(limit_choices_to={'user_profile': 'SU'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
