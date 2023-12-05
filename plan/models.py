from django.db import models

from user.models import User

# Create your models here.


class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()
    destination = models.CharField(max_length=20, default='destination')
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    user = models.ManyToManyField(
        User, related_name="plan_u")  # Related name is
    # to change the name of model class in query set API

    def created_by(self):
        return ','.join([str(u) for u in self.user.all()])

    # createdAt = models.DateTimeField(auto_now_add=True)
    # updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
