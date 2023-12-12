from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import Student
from .serializers import Studentserializers


class CommonView(GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializers

    def get(self, request, *args, **kargs):
        return self.list(request, *args, **kargs)

    def post(self, request, *args, **kargs):
        return self.create(request, *args, **kargs)

    def put(self, request, *args, **kargs):
        return self.update(request, *args, **kargs)

    def delete(self, request, *args, **kargs):

        return self.destroy(request, *args, **kargs)
