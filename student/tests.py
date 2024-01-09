from django.test import TestCase

# Create your tests here.
# tests.py
import pytest
from rest_framework.test import APIClient
from student.models.models import *
from .serializers import StudentSerializer


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_data():
    return {'name': 'Lokesh', 'age': 22, 'address': 'remote'}


def test_create_student(client, student_data):
    response = client.post('/api/v1/student/add/', student_data)
    assert response.status_code == 201
    assert Student.objects.count() == 1
    assert Student.objects.get().name == student_data['name']


def test_get_student(client, student_data):
    student = Student.objects.create(**student_data)
    response = client.get(f'/api/v1/student/{student.id}/')
    assert response.status_code == 200
    assert response.data == StudentSerializer(student).data


def test_list_students(client, student_data):
    student1 = Student.objects.create(**student_data)
    student2 = Student.objects.create(**student_data)
    response = client.get('/api/v1/students/')
    assert response.status_code == 200
    assert response.data == StudentSerializer(
        [student1, student2], many=True).data


def test_update_student(client, student_data):
    student = Student.objects.create(**student_data)
    updated_data = {'name': 'demo', 'age': 21, 'address': 'remote'}
    response = client.put(f'/api/v1/update/{student.id}/', updated_data)
    assert response.status_code == 200
    assert Student.objects.get().name == updated_data['name']
    assert Student.objects.get().age == updated_data['age']


def test_delete_student(client, student_data):
    student = Student.objects.create(**student_data)
    response = client.delete(f'/api/v1/delete/{student.id}/')
    assert response.status_code == 204
    assert Student.objects.count() == 0
