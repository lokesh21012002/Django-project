from rest_framework import serializers
from .models import Student, Course


# we cn use validators here also
# field level validation
# object level validation
# validators

# validators>field>object


class CourseSerializer(serializers.Serializer):
    stu = serializers.StringRelatedField(many=True, read_only=True)
    stu = serializers.PrimaryKeyRelatedField()
    stu = serializers.HyperlinkedRelatedField()
    stu = serializers.SlugRelatedField()

    class Meta:
        model = Course
        fields = '__all__'


class Studentserializers(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        # incldue=['id','name','age']
        # exclude=['address']
        read_only_fields = ['id']
        # Extra arguments to fields
        # extra_kargs = {'id': {read_only_fields: True}}

    def validate_age(self, value):  # field level validation

        if type(value) == int:
            return value
        else:
            raise serializers.ValidationError("Age should be integer")

        # if type(value) != int:
        #     print("Hello")
        #     raise serializers.ValidationError("Age should be integer")
        #     # return value
        # if value < 0:
        #     raise serializers.ValidationError("Age should be positive")

        # return value

    # def validate(self, data):
    #     name = data.get('name')
    #     age = data.get('age')
    #     if type(age) != int:
    #         raise serializers.ValidationError("Age must be integer")

    #     if age < 0:
    #         raise serializers.ValidationError("Age must be positive")

    #     return data

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.address = validated_data.get('address', instance.address)

    #     instance.save()
    #     return instance

    # def create(self, **validated_data):
    #     return super().create(validated_data)


class Demo(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
