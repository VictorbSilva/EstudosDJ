# Generated by Django 5.1.6 on 2025-02-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cepmodel',
            name='cep',
            field=models.CharField(max_length=9),
        ),
    ]
