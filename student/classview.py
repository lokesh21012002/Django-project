
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from .serializers import Studentserializers
from .models import Student
import json


from django.views import View


@method_decorator(csrf_exempt, name="dispatch")
class StudentView(View):

    def get(self, request, *args, **kargs):
        if request.method == 'GET':

            students = Student.objects.all()
            print(students)

            serialize = Studentserializers(students, many=True)

            print(serialize.data)
            return JsonResponse(serialize.data, safe=False, status=200)

        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)

    def post(self, request, *args, **kargs):
        if request.method == 'POST':
            payload = json.loads(request.body)
            print(payload)
            # print(request.body)

            serialized_data = Studentserializers(data=payload)
            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse({"message": "success"}, status=201)
            else:
                return JsonResponse(serialized_data.errors, status=400)

        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)

    def put(self, request, *args, **kargs):
        if request.method == 'PUT':
            print(id)
            payload = json.loads(request.body)
            print("Payload", payload)
            if len(Student.objects.filter(id=id)) == 0:
                return JsonResponse({"error": "Student not found"}, status=404)

            serializer = Studentserializers(
                instance=Student.objects.get(id=id), data=payload)
            print(serializer)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Updated Successfully!"}, status=200)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({"Error": "Invalid Method"}, status=400)

    def delete(selft, request, *args, **kargs):
        print(id)
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({"message": "Successfully deleted the student."}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
