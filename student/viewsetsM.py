from rest_framework import viewsets
from .models import Person, Colour
from .serializers import PersonSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from django.db.models import Subquery, OuterRef


class CustomeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthticate]
    authentication_classes = [TokenAuthetication]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # by default modelviewset provide all to restrict it
    http_method_names = ['GET', 'POST']

    def list(self, request):

        print(request.user)
        serach_param = request.GET.get("search")
        queryset = self.queryset

        if serach_param:
            queryset.filter(name__startswith=serach_param)

        serialize = PersonSerializer(queryset, many=True)

        return Response(serialize.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])  # to implement our own methods
    def send_mail(self, request):

        return Response({"msg": "Sucesss"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def send_message(request):
        return Response({"msg": "Sucess"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET"

                                  ])
    def custom_metod(self, request):
        colour = Colour.objects.filter(id=request.get('id'))
        persons = Person.objects.filter(id__in=Subquery(colour.values("id")))
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):

    def post(self, request):
        data = request.data
        user = authenticate(
            username=data['username'], password=data['password'])
        if user is not None:
            token, _ = Token.objects.get_or_create(user)
            return Response({
                "msg": "Sucess",
                "token": str(token)



            }, status=status.HTTP_201_CREATED)
        else:

            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)


class SignupView(APIView):

    def post(self, request):
        data = request.data
        user = UserSerializer(data=data)

        if user.is_valid():
            return Response({"msg": user.erros}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.save()
            return Response({"message": "Sign up Success!"}, status=status.HTTP_201_CREATED)
