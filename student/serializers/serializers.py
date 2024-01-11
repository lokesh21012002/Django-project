from django.contrib.auth.models import User

from rest_framework import serializers
# from .models import Student, Course
from student.models.models import *


# # we cn use validators here also
# # field level validation
# # object level validation
# # validators

# # validators>field>object


class CourseSerializer(serializers.Serializer):
    stu = serializers.StringRelatedField(many=True, read_only=True)
    # stu = serializers.PrimaryKeyRelatedField()
    # stu = serializers.HyperlinkedRelatedField()
    # stu = serializers.SlugRelatedField()

    class Meta:
        model = Course
        fields = '__all__'


# class AdminSerializer(serializers.Serializer):


class Studentserializers(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = StudentModel
        fields = '__all__'
#         # incldue=['id','name','age']
#         # exclude=['address']
#         read_only_fields = ['id']
#         # Extra arguments to fields
#         # extra_kargs = {'id': {read_only_fields: True}}

    # def validate_age(self, value):  # field level validation

    #     if type(value) == int:
    #         return value
    #     else:
    #         raise serializers.ValidationError("Age should be integer")

#         # if type(value) != int:
#         #     print("Hello")
#         #     raise serializers.ValidationError("Age should be integer")
#         #     # return value
#         # if value < 0:
#         #     raise serializers.ValidationError("Age should be positive")

#         # return value

    def validate(self, data):
        print(data)
        name = data.get('name')
        age = data.get('age')
        if type(age) != int:
            raise serializers.ValidationError("Age must be integer")

        if age < 0:
            raise serializers.ValidationError("Age must be positive")

        return data

#     # def update(self, instance, validated_data):
#     #     instance.name = validated_data.get('name', instance.name)
#     #     instance.age = validated_data.get('age', instance.age)
#     #     instance.address = validated_data.get('address', instance.address)

#     #     instance.save()
#     #     return instance

#     # def create(self, **validated_data):
#     #     return super().create(validated_data)


# class Demo(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'


# class UserSerializer(serializers.ModelField):

    # class Meta:
    #     model = UserModel
    #     fields = '__all__'

    # def validate(self, obj):
    #     if obj.get('username'):

    #         user = User.objects.get(username=obj['username'])
    #         raise serializers.ValidationError(
    #             {"message": "Username already exists."})
    #     if obj.get('email'):
    #         user = User.objects.get(username=obj['email'])
    #         raise serializers.ValidationError(
    #             {"message": "Email already exists."})

    #     return user

    # def create(self, validated_data):
    #     user = UserModel.objects.create(
    #         validated_data['username'], validated_data['email'])
    #     user.set_password(validated_data['password'])

    #     user.save()

    #     return user


# class ColourSerializer(serializers.ModelSerializer):

    # class Meta:
    #     model = Colour
    #     fields = ['colour_name']


# class PersonSerializer(serializers.ModelSerializer):
    # colour = ColourSerializer(many=True)
    # country = serializers.SerializerMethodField()

    # class Meta:
    #     model = Person
    #     fields = '__all__'
    #     depth = 1  # shows all fields of Foreign Table

    # def get_country(self, obj):
    #     return {"name": "India"}

    # def validate_name(self, name):
    #     special = "~!@#$%^&?<>/?|"
    #     for letter in name:
    #         if letter in special:
    #             raise serializers.ValidationError(
    #                 "Name cannot contain any of these characters ~!@#$%^&?<>/\|")

    #     return name

    # def validate(self, data):
    #     if data['age'] < 18:
    #         return serializers.ValidationError("Age should be greater than 18")

    #     return data
