# Generated by Django 4.2.7 on 2023-12-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_phone'),
        ('plan', '0003_plan_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='user',
        ),
        migrations.AddField(
            model_name='plan',
            name='user',
            field=models.ManyToManyField(to='user.user'),
        ),
    ]
