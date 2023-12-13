from rest_framework import viewsets
from .models import Student
from .serializers import Studentserializers
from rest_framework import authentication, authtoken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
# from .customauth import JWTAuthentication

from rest_framework_simplejwt.authentication import JWTAuthentication


class viewSetStudent(viewsets.
                     #  ModelViewSet
                     ReadOnlyModelViewSet
                     ):
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = Studentserializers


class AuthViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]  # override from global settings
    serializer_class = Studentserializers
    queryset = Student.objects.all()
