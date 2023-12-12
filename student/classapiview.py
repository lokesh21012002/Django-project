from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class APiClassView(APIView):
    def get(self, request, format=None):
        return Response({'message': 'GET Method Called Successfully!'}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response({'message': 'GET Method Called Successfully!'}, status=status.HTTP_201_CREATED)
