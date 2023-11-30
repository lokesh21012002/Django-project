from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def hello(request):

    # print(request)
    a = "Hello World from user"
    return HttpResponse(f'{a}')


def name(request):
    print(type(request))

    return JsonResponse({'text': "Lokesh Gawande", 'response': 200})


def dynamic(request):

    # if request.method == 'GET':
    #     data = {'name': 'lokesh', 'age': 35}
    #     return JsonResponse(data)

    return JsonResponse({"status": 200})
