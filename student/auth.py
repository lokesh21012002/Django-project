from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class CustomAuth(ObtainAuthToken):
    def post(self, request, *args, **kargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token,
                         'id': user.get('id'),
                         'name': user.get('password'),

                         }, status=status.HTTP_201_CREATED)
