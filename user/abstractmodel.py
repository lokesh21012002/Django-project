from django.db import models


class abstractModel(models.Model):
    username = models.CharField(max_length=20, default="root")
    password = models.CharField(max_length=20, default="password")
    email = models.EmailField(default="admin@gmail.com")

    class Meta:
        abstract = True
