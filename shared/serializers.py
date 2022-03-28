from uuid import uuid4
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import *

class ClientSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    client_class = serializers.CharField(required=False)

    class Meta:
        model = Client
        fields = '__all__'
