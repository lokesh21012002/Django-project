from django.shortcuts import render
from django.http import request, JsonResponse, HttpResponse
from datetime import datetime
from rest_framework.response import Response
from student.models.models import *
# from .serializers import Studentserializers
from student.serializers.serializers import *
import json
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import sync_to_async
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache


# Create your views here.
# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def helper(serialized_data):
    return {"id": serialized_data.data.get("id"),
            "name": serialized_data.data.get("name"),
            "age": calculate_age(serialized_data.data.get('dob')),
            "address": serialized_data.data.get('address')





            }


def heleperall(obj):
    return {"id": obj.get("id"),
            "name": obj.get("name"),
            "age": calculate_age(obj.get('dob')),
            "address": obj.get('address')





            }


def calculate_age(dob):
    cus_date = datetime.strptime("2002-01-21", "%Y-%m-%d").date()
    # print(type(cus_date))
    # print(type(date.today()), type*)
    # dobnew = tuple(map(int, dob.split(',')))
    age = relativedelta(date.today(), cus_date)
    print(age.years)
    return age.years


@csrf_exempt
def getAllStudents(request):
    try:
        if request.method == 'GET':

            students = StudentModel.objects.all()
            print(students)

            serialize = Studentserializers(students, many=True)

            # print(serialize.data)
            students_response = []
            for i in serialize.data:
                students_response.append(heleperall(i))
                # print(heleperall(i))
            #     students_response.append(helper(i))
            # students_response.append(he)
            # students_response.append(ResponseEntity(
            #     i.id, i.name, calculate_age(i.dob), i.address))
            return JsonResponse(students_response, safe=False, status=200)

        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    # print(json.dumps(serialize.data))
    # print(serialize.data)
    # # print(json.dumps(serialize.data))
    # for i in serialize.data:
    #     print(i)

    # return JsonResponse(serialize.data, safe=False)
    # return HttpResponse(serialize.data)

    # return "JsonResponse(serialize.data)"


# @csrf_exempt
# def getStudentById(request, id):
#     if request.method == "GET":

#         # if cache.get(id):
#         #     print("data from cache")
#         #     student = cache.get(id)
#         #     return JsonResponse(student.data)
#         # else:

#         try:

#             stu = StudentModel.objects.filter(id=id)
#             print(stu)
#             if len(stu) == 0:
#                 return JsonResponse({"msg": "Student not Found"}, status=200)
#             else:
#                 serialized_data = Studentserializers(stu[0])
#                 # cache.set(id, serialized_data)

#                 return JsonResponse(serialized_data.data, status=200, safe=False)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

#     else:
#         return JsonResponse('Not Allowed', safe=False, status=403)


# @csrf_exempt
# def addStudent(request):
#     # if request.method == 'POST':
#     # data = json.loads(request.body)

#     if request.method == 'POST':
#         try:
#             payload = json.loads(request.body)

#             # print(request.body)
#             if type(payload["age"]) != int:
#                 raise ValueError("Age must be an integer")

#             serialized_data = Studentserializers(data=payload)
#             if serialized_data.is_valid(raise_exception=True):
#                 serialized_data.save()
#                 return JsonResponse({"message": "success", "data": serialized_data.data}, status=201)
#             else:
#                 # serialized_data.save()
#                 # serialized_data.create()
#                 # StudentModel.objects.create(serialized_data)
#                 # serialized_data.create(serialized_data.validated_data)
#                 return JsonResponse(serialized_data.errors, status=400, safe=False)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

#     else:
#         return JsonResponse({"error": "Method not allowed"}, status=405)


# @csrf_exempt
# def deleteStudent(request, id):
#     print(id)
#     try:
#         student = StudentModel.objects.get(id=id)
#         student.delete()
#         return JsonResponse({"message": "Successfully deleted the student."}, status=204)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @csrf_exempt
# def updateStudent(request, id):
#     if request.method == 'PUT':

#         try:
#             print(id)
#             payload = json.loads(request.body)
#             print("Payload", payload)
#             if len(StudentModel.objects.filter(id=id)) == 0:
#                 return JsonResponse({"error": "Student not found"}, status=404)

#             serializer = Studentserializers(
#                 instance=StudentModel.objects.get(id=id), data=payload)
#             print(serializer)

#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({"message": "Updated Successfully!"}, status=204)
#             else:
#                 return JsonResponse(serializer.errors, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#     else:
#         return JsonResponse({"Error": "Invalid Method"}, status=400)

    # print(request.data)

    # print(id)
    # return JsonResponse({})\


@csrf_exempt
def studentAPI(request, id=0):
    print(id)
    if request.method == 'GET':
        try:
            print(id)

            stu = StudentModel.objects.filter(id=id)
            print(stu)
            if len(stu) == 0:
                return JsonResponse({"msg": "Student not Found"}, status=200)
            else:
                serialized_data = Studentserializers(stu[0])
                # cache.set(id, serialized_data)
                # student = ResponseEntity(serialized_data.data.id, serialized_data.data.name, calculate_age(
                #     serialized_data.data.dob), serialized_data.data.address)

                return JsonResponse(helper(serialized_data), status=200, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == 'POST':
        try:
            payload = json.loads(request.body)

            # print((payload['dob']))
            print(payload)
            # if type(payload["dob"]) in ['str', 'int']:

            #     raise ValueError("Invalid DOB")

            serialized_data = Studentserializers(data=payload)
            if serialized_data.is_valid(raise_exception=True):
                serialized_data.save()
                # student = ResponseEntity(serialized_data.data.get('id'), serialized_data.data.get("name"), calculate_age(
                #     serialized_data.data.get("dob")), serialized_data.data.get("address"))
                return JsonResponse(helper(serialized_data), safe=False, status=201)
            else:
                # serialized_data.save()
                # serialized_data.create()
                # StudentModel.objects.create(serialized_data)
                # serialized_data.create(serialized_data.validated_data)
                return JsonResponse(serialized_data.errors, status=400, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == 'PUT':
        try:
            print(id)
            payload = json.loads(request.body)
            print("Payload", payload)
            if len(StudentModel.objects.filter(id=id)) == 0:
                return JsonResponse({"error": "Student not found"}, status=404)

            serializer = Studentserializers(
                instance=StudentModel.objects.get(id=id), data=payload)
            print(serializer)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Updated Successfully!"}, status=200)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == 'DELETE':
        try:
            student = StudentModel.objects.get(id=id)
            student.delete()
            return JsonResponse({"message": "Successfully deleted the student."}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    else:

        return JsonResponse({"Error": "Invalid Method"}, status=400)
