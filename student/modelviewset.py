from rest_framework import viewsets
from .models import Student
from .serializers import Studentserializers
from rest_framework import authentication, authtoken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BaseAuthentication


class viewSetStudent(viewsets.
                     #  ModelViewSet
                     ReadOnlyModelViewSet
                     ):
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = Studentserializers


class AuthViewSet(viewsets.ModelViewSet):
    authentication_classes = [BaseAuthentication]
    permission_classes = [AllowAny]  # override from global settings
    serializer_class = Studentserializers
    queryset = Student.objects.all()
