# Generated by Django 4.1.4 on 2023-01-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_appointment_doctor_alter_appointment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
