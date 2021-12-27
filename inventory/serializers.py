from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import Line, Product

class ProductSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    line_id = serializers.UUIDField()
    name = serializers.CharField()
    category = serializers.CharField()
    description = serializers.CharField()
    quantity = serializers.CharField()
    brochure = serializers.CharField()
    
    class Meta:
        fields = '__all__'
        model = Product

class LineSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        models = Line
