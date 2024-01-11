from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date

# Create your models here.


def calculate_age(value):
    age = relativedelta(date.today()-value).years
    return age


def validate_age(value):
    # print(type(value))
    if type(value) != date or calculate_age(value) <= 0 or calculate_age(value) > 50:
        raise Exception("Invalid age")

    return value


# class Student(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)

#     address = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name
class StudentModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    dob = models.DateField()

    address = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    duration = models.CharField(max_length=5)
    student = models.ManyToManyField(
        StudentModel)

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


class ResponseEntity:
    id = int
    name = str
    age_stu = int
    address = str

    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age_stu = age
        self.address = address
