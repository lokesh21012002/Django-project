from rest_framework import viewsets
from .models import Student, Course
from .serializers import Studentserializers, CourseSerializer
import redis
from django.core.cache import cache
import time

from rest_framework.response import Response

from rest_framework import status

redisInstance = redis.StrictRedis('127.0.0.1', port=6279, db=1)


class StudentViewset(viewsets.ModelViewset):
    queryset = Student.objects.all()
    serializer_class = Studentserializers

    def getByID(self, request, id):
        key = "student_{}".format(id)
        student = cache.get(key)
        if not student:
            student = Student.objects.get(pk=id)
            serialized_data = Studentserializers(data=student)
            cache.set(key, serialized_data.data, time.hour*4)
            print("data from DB")
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:

            print("data from cache")

            return Response(cache.get(key), status=status.HTTP_200_OK)


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
