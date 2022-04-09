from rest_framework import serializers

from .models import Line, Product

class ProductSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    line_id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    quantity = serializers.CharField(required=False)
    brochure = serializers.CharField(required=False)
    
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
