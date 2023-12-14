from rest_framework import viewsets
from .models import Student
from .serializers import Studentserializers
from rest_framework.generics import ListAPIView
from rest_framework import authentication, authtoken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
# from .customauth import JWTAuthentication

from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import PageClass
from .LimitOffsetPagination import LimitOffsetPagination


class viewSetStudent(viewsets.
                     #  ModelViewSet
                     ReadOnlyModelViewSet, ListAPIView
                     ):
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = Studentserializers
    # filter_backends = [DjangoFilterBackend]
    # filter_backends = [SearchFilter]
    filter_backends = [OrderingFilter]
    # search_fields = ['city', "age", '^address', '=age',]
    ordering_fields = ['name']
    ordering_fields = ['name', 'age']
    ordering_fields = '__all__'
    # pagination_class = PageClass
    pagination_class = LimitOffsetPagination

    # ^ sttarts with = exact match
    # filterset_fields = ['name', 'age']

    # def get_queryset(self):
    #     # return self.queryset.filter(user=request.user)
    #     return Student.objects.filter(id=self.request.data)


class AuthViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]  # override from global settings
    serializer_class = Studentserializers
    queryset = Student.objects.all()
