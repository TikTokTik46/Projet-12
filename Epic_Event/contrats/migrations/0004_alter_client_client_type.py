# Generated by Django 4.2.2 on 2023-06-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrats', '0003_alter_client_client_type_delete_clienttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_type',
            field=models.CharField(choices=[('NW', 'Sans contrats'), ('EX', 'Avec contrats')], max_length=2),
        ),
    ]
