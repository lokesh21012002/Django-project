# Generated by Django 4.2.7 on 2023-12-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_email_alter_user_id_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='9977661182', max_length=10),
        ),
    ]
