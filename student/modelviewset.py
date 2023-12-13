from rest_framework import viewsets
from .models import Student
from .serializers import Studentserializers


class viewSetStudent(viewsets.
                     #  ModelViewSet
                     ReadOnlyModelViewSet
                     ):
    queryset = Student.objects.all()
    serializer_class = Studentserializers
