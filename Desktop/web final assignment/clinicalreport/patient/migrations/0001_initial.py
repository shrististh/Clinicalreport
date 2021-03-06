# Generated by Django 3.0.7 on 2020-07-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]
