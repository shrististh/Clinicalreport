# Generated by Django 3.0.7 on 2020-08-02 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='mname',
        ),
    ]
