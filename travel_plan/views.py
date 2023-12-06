from django.http import *
import json


def helloJoson(request):
    jsonBody = {'name': 'lokesh', 'status': 200}

    return HttpResponse(json.dumps(jsonBody))  # convert object  to json


def parseJson(request):
    jsonBody = json.dumps({'name': 'lokesh', 'status': 200})
    # convert json to  object or string
    return HttpResponse(json.loads(jsonBody))
