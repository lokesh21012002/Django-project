# Generated by Django 4.2.7 on 2023-11-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='destination',
            field=models.CharField(default='destination', max_length=20),
        ),
    ]
