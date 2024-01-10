from django.db import models

# Create your models here.


def validate_age(value):
    # print(type(value))
    if type(value) != int or value < 0 or value > 100:
        raise Exception("Invalid age")

    return value


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[validate_age])
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    duration = models.CharField(max_length=5)
    student = models.ManyToManyField(
        Student)

    def __str__(self):
        return f"{self.id} {self.name}"


# class Colour(models.Model):
#     colour_name = models.CharField(max_length=10)

#     def __str__(self):
#         return self.colour_name


# class Person(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=10)
#     age = models.IntegerField()
#     address = models.CharField(max_length=20)
#     colour = models.ForeignKey(
#         Colour, null=True, blank=True, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=20, unique=True, blank=False)
#     email = models.EmailField()
#     password = models.CharField(max_length=10, blank=False)

#     def __str__(self):
#         return self.username