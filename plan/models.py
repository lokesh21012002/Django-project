from django.db import models

# Create your models here.


class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    destination = models.CharField(max_length=20, default='destination')

    def __str__(self):
        return self.name
