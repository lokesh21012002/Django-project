# Generated by Django 4.2.7 on 2024-01-11 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='age',
            new_name='dob',
        ),
    ]