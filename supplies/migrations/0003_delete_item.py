# Generated by Django 4.1.4 on 2023-01-14 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0002_alter_item_current_capacity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]