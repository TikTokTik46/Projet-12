# Generated by Django 4.2.2 on 2023-06-30 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('évènements', '0004_alter_event_event_status_delete_eventstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_status',
            field=models.CharField(choices=[('PR', 'En preparation'), ('IP', 'En cours'), ('FN', 'Terminé')], max_length=2),
        ),
    ]
