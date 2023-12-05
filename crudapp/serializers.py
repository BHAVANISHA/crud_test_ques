from crudapp import models
from crudapp.models import PlacementDetails
from rest_framework import serializers
class Placeserializer(serializers.ModelSerializer):
    class Meta:
        model=PlacementDetails
        fields='__all__'
class Custom1(serializers.Serializer):
    candidate_name=serializers.CharField()
    rename_name=serializers.CharField()
class Customnamedetail(serializers.Serializer):
    candidate_name=serializers.CharField()

class Customnamebusiness(serializers.Serializer):
    candidate_name=serializers.CharField()
    business_unit=serializers.CharField()

class CustomMasonite(serializers.Serializer):
    client=serializers.CharField()