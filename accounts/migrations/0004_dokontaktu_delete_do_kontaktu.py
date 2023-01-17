# Generated by Django 4.1.4 on 2023-01-16 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_do_kontaktu'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoKontaktu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60)),
                ('skontaktowano', models.BooleanField(default=False)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Data rejestracji')),
            ],
            options={
                'verbose_name': 'Do kontaktu',
                'verbose_name_plural': 'Użytkownicy do kontaktu',
            },
        ),
        migrations.DeleteModel(
            name='Do_Kontaktu',
        ),
    ]