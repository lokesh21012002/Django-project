from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import Studentserializers
from rest_framework_simplejwt.tokens import RefreshToken


# class CustomAuth(ObtainAuthToken):
#     def post(self, request, *args, **kargs):
#         serializer = self.serializer_class(
#             data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token,
#                          'id': user.get('id'),
#                          'name': user.get('password'),

#                          }, status=status.HTTP_201_CREATED)


def getToken(User):
    genToken = RefreshToken.for_user(User)
    return {
        'refresh': str(genToken),
        'access': str(genToken.access_token)
    }


class Register(APIView):
    def post(self, request):
        userdata = request.data['userdata']
        roledata = request.data['roledata']
        admin = True if userdata['role'] == 'Admin' else False

        userdata['avatar'] = "https://api.dicebear.com/6.x/pixel-art/svg?seed=" + \
            userdata['name']

        userserialize = Studentserializers(data=userdata)
        roleserializer = None

        if userserialize.is_valid(raise_exception=True):

            if admin:
                roleserializer = AdminSerializer(data=roledata)
            else:
                roleserializer = Studentserializers(data=roledata)

            if roleserializer.is_valid(raise_exception=True):
                user = userserialize.save()
                roleserializer.validated_data['user'] = user
                roleserializer.save()
                token = getToken(user)
                return Response({'token': token, 'status': 'ok', 'message': 'User created successfully', 'user': userserialize.data}, status=status.HTTP_200_OK)

        return Response(userserialize.errors, status=status.HTTP_401_UNAUTHORIZED)
