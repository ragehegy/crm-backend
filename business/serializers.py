from uuid import uuid4
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from shared.serializers import ClientSerializer

from .models import BusinessClient, DistrictEmplyoee, Employee, LeaveRequest, Request, Unit


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


class EmployeeSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(max_length=255, required=False)
    username = serializers.CharField(max_length=255, required=False)
    phone = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Employee
        fields = '__all__'


class RequestQuerySerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    employee__id = serializers.UUIDField(required=False)

class LeaveRequestQuerySerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    requset__id = serializers.UUIDField(required=False)


class RequestSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False, default=uuid4)
    employee = EmployeeSerializer(required=False)
    type = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    created = serializers.DateTimeField(required=False)
    
    class Meta:
        fields = '__all__'
        model = Request


    def create(self, validated_data):
        employee = validated_data.pop('employee', None)
        validated_data['employee_id'] = employee['id']
        request = Request(**validated_data)
        request.save()
        return request


class LeaveRequestSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False, default=uuid4)
    request = RequestSerializer(required=False)
    leave_type = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    
    class Meta:
        fields = '__all__'
        model = LeaveRequest


    def create(self, validated_data):
        request = validated_data.pop('request', None)
        request = RequestSerializer(data=request)
        request.is_valid()
        request.save()

        validated_data['request_id'] = request.data['id']
        leave_request = LeaveRequest(**validated_data)
        leave_request.save()
        
        return leave_request

class BusinessClientSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False, source='client.name')
    address = serializers.CharField(required=False, source='client.address')
    email = serializers.CharField(max_length=255, required=False, source='client.email')
    phone = serializers.CharField(max_length=255, required=False, source='client.phone')
    type = serializers.CharField(max_length=255, required=False, source='client.type')
    client_class = serializers.CharField(max_length=255, required=False, source='client.client_class')

    class Meta:
        model = BusinessClient
        exclude = ('business', 'client')