# Generated by Django 4.2.2 on 2023-06-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
