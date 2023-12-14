

from .models import Student
from .serializers import Studentserializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication


class ProdView(viewsets.ModelViewSet):
    # model = Student
    serializer_class = Studentserializers
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
