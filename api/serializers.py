from pyexpat import model
from statistics import mode
from rest_framework import serializers
from little.models import PersonModel

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = '__all__'





