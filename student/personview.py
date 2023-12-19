

from .models import Person
from .serializers import PersonSerializer

from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def getAllPersons(request):

    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getById(request, id):

    search_param = request.GET.get("search")
    try:
        person = Person.objects.get(pk=id)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Person.DoesNotExist:
        return Response({"error": "Person does not exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addPerson(request):
    data = request.data

    try:
        serializer = PersonSerializer(data=data, many=False)
        if serializer.is_valid(raise_exception=True):  # validate the input data
            serializer.save()                         # save it to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
          # return a response with the data

        else:
            return Response({"msg": "invalid"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("Error in adding new person")
        return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


# update an existing object by id
@api_view(['PUT', 'PATCH'])
def updatePerson(request, id):
    try:
        person = Person.objects.get(pk=id)
        s = PersonSerializer(person, context={'request': request})
        d = s.to_representation(person)
        # check for PUT or PATCH method
        if request.method == 'PUT':
            # create a new serializer with the full data from the client
            new_s = PersonSerializer(
                data=d['data'], context={'request': request})
            # validate and set the password again because it is required field while updating
            if new_s.is_valid(raise_exception=True):
                new_s.initial_data['password'] = new_s.validated_data.pop(
                    'password', None)
                # update the fields of the existing object using the validated data from the new serializer
                for k in new_s.validated_data.keys():
                    setattr(person, k, new_s.validated_data[k])
                person.save()
                return Response(new_s.data, status=status.HTTP_200_OK)
        elif request.method == 'PATCH':
            patch_data = dict((k, v)for k, v in request.data.items() if k in d['fields'].keys
                              ())
            patch_s = PersonSerializer(
                person, data=patch_data, context={'request': request})
            if patch_s.is_valid(raise_exception=True):
                # if there are no common fields between the old and new data then just return the old data
                if patch_s.validated_data == {}:
                    return Response(patch_data.data, status=status.HTTP_200_OK)
                else:
                    # otherwise update only the common fields
                    return Response(patch_s.data, status=status.HTTP_200_OK)
            # return a response containing the updated common fields
    except Person.DoesNotExist:
        return Response({"msg": "NOt Found"}, status.HTTP_404_NOT_FOUND)
# return a response that the user does not exist
    except Exception as e:
        print("Error in updating person ", e)


@api_view(["DELETE"])
def deletePerson(request, id):
    try:
        person = Person.objects.get(pk=id)
        person.delete()
        return Response({"msg": "Deleted Successfully!"}, status.HTTP_200_OK)
    except Person.DoesNotExist:
        return Response({"msg": "User Does Not Exists"}, status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": "Error In Deleting User"}, status.HTTP_503_SERVICE_UNAVAILABLE)
