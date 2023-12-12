from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import Studentserializers

# by default it only support get method
# @api_view(['GET', 'POST'])
# def hello(request):

# print(request.query_params())

# if request.method == 'GET':
#     return Response({"message": "Hello! This is a simple Hello World API."}, status=status.HTTP_200_OK)

# else:
#     return Response({"msg": "This is hello from post"}, status=status.HTTP_202_ACCEPTED, headers={}, content_type="application/json")

# return Response({"msg": "Bad resuqest"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", 'POST', 'PUT', "DELETE"])
def CRUD_API(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is None:
            stu = Student.objects.all()
            serialize_data = Studentserializers(stu, many=True)
            return Response(serialize_data.data, status=status.HTTP_200_OK)
        else:
            stu = Student.objects.get(id)
            serialize_data = Studentserializers(stu)
            return Response(serialize_data.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        payload = request.data
        validate_data = Studentserializers(data=payload)
        if validate_data.is_valid():
            validate_data.save()
            return Response(validate_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(validate_data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = request.data.get("id")
        if id is None:
            return Response({"msg": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            student = Student.objects.get(id=id)
            student.name = request.data['name']
            student.age = request.data['age']
            student.address = request.data['address']
            student.save()
            serialize_data = Studentserializers(student)
            return Response(serialize_data.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        id = request.data.get("id")
        if id is None:
            return Response({"msg": "Student not Found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            Student.objects.filter(id=id).delete()
            return Response("Delete Successfully", status=status.HTTP_200_OK)
    else:
        return Response({"msg": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
