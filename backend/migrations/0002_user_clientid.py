# Generated by Django 3.1.2 on 2020-11-13 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='clientID',
            field=models.ForeignKey(default='PLACEHOLDER', on_delete=django.db.models.deletion.CASCADE, to='backend.client'),
        ),
    ]
