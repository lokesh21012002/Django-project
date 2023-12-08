from rest_framework import serializers
from .models import Student


class Studentserializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.address = validated_data.get('address', instance.address)

        instance.save()
        return instance

    # def create(self, **validated_data):
    #     return super().create(validated_data)
