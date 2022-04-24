from rest_framework import serializers

from .models import *

class ClientSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    client_class = serializers.CharField(required=False)

    class Meta:
        model = Client
        fields = '__all__'

class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    governorate = GovernorateSerializer()
    class Meta:
        model = City
        fields = '__all__'
