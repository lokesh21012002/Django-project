from rest_framework.viewsets import ViewSet
from .models import Student
from .serializers import Studentserializers
from rest_framework.response import Response
from rest_framework import status


class viewClassSet(ViewSet):
    def list(self, request, pk=None):

        print(self.action)
        print(self.basename)
        print(self.description)
        print(self.suffix)
        print(self.detail)

        id = pk
        if id is None:
            stu = Student.objects.all()
            stud_serial = Studentserializers(stu, many=True)
            return Response(stud_serial.data, status=status.HTTP_200_OK)
        else:
            stu = Student.objects.filter(pk=id).first()
            if stu is None:
                return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                stud_serialize = Studentserializers(stu)
                return Response(stud_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        serilize = Studentserializers(data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response(serilize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilize.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        id = pk
        if id is None:
            return Response({"msg": "Invalid"}, status=status.HTTP_404_NOT_FOUND)
        else:
            std = Student.objects.filter(pk=id).first()
            if std is None:
                return self.create(request)
            serilize = Studentserializers(std, data=request.data)
            serilize.is_valid(raise_exception=True)
            serilize.save()
            return Response(serilize.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response({"msg": "Updated"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        id = pk
        if id is None:
            return Response({"msg": "Invalid"}, status=status.HTTP_404_NOT_FOUND)
        else:
            std = Student.objects.filter(pk=id).delete()
            if std == 0:
                return Response({"msg": "No data Deleted"}, status=status.HTTP_404_NOT_FOUND)
            elif std > 1:
                return Response({"msg": 'Data deleted Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({"msg": 'Only one record can be deleted at a time.'}, status=status.HTTP_200_OK)
