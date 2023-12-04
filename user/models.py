from django.db import models

from user.abstractmodel import abstractModel

# Create your models here.


class User(abstractModel):

    # id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=20, unique=True)
    # password = models.CharField(max_length=16)
    # email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, default="9977661182")

    def __str__(self):
        return self.username
