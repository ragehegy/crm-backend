from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import DistrictEmplyoee, Unit


class DistrictEmployeesSerializer(serializers.Serializer):
    district = serializers.UUIDField(required=True)
    employees = serializers.ListField(child=serializers.UUIDField())

    class Meta:
        model = DistrictEmplyoee

    def create(self, validated_data):
        data = [
            self.Meta.model(district_id = validated_data.get('district'), employee_id=employee)
            for employee in validated_data.get('employees')
        ]
        return self.Meta.model.objects.bulk_create(data)

class UnitSerializer(serializers.Serializer):
    business = serializers.UUIDField(required=True)
    name = serializers.CharField(required=True)
    head = serializers.UUIDField()

    class Meta:
        model = Unit

    def create(self, validated_data):
        return super().create(validated_data)