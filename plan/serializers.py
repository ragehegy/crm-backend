from uuid import uuid4
from rest_framework import serializers

from .models import *
from business.serializers import BusinessClientSerializer, EmployeeSerializer
from inventory.serializers import ProductSerializer

class VisitLogSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False, default=uuid4)
    status = serializers.CharField(required=True)
    timestamp = serializers.DateTimeField(required=False)
    feedback = serializers.CharField(required=False)

    class Meta:
        model = VisitLog
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = data.get('status', None).lower()
        return data

    def create(self, validated_data):
        log = VisitLog.objects.create(**validated_data)
        log.save()
        return log

class VisitProductSerializer(serializers.Serializer):
    # id = serializers.UUIDField(required=False, default=uuid4)
    product_details = ProductSerializer(source='product')
    feedback = serializers.CharField(required=False)
    notes = serializers.CharField(required=False)

    class Meta:
        model = VisitProduct
        fields = '__all__'

class VisitQuerySerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    status = serializers.CharField(required=False)
    from_time = serializers.DateTimeField(required=False)
    to_time = serializers.DateTimeField(required=False)
    datetime__range = serializers.ListField(child=serializers.DateTimeField(), required=False)
    employee_id = serializers.UUIDField(required=False)

    def to_representation(self, instance):
        instance.update({
            'datetime__range': [instance.pop('from_time'), instance.pop('to_time')]
        })

        # instance.update({
        #     'plan__parent_plan__employee__id': instance.pop('employee_id')
        # })
        return super(VisitQuerySerializer, self).to_representation(instance)

class VisitSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False, default=uuid4)
    plan_id = serializers.UUIDField(required=True)
    client_id = serializers.UUIDField(required=True, write_only=True)
    status = serializers.CharField(required=False)
    approval_status = serializers.CharField(required=False)
    type = serializers.ChoiceField(required=True, choices=VisitAgenda.VISIT_TYPES)
    datetime = serializers.DateTimeField(required=False)
    notes = serializers.CharField(required=False)
    client = BusinessClientSerializer(read_only=True)
    products = VisitProductSerializer(many=True, required=False, read_only=True)
    logs = VisitLogSerializer(many=True, required=False)

    class Meta:
        model = VisitAgenda
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = data.get('status', None).lower()
        data['approval_status'] = data.get('approval_status', None).lower()
        data['type'] = data.get('type', None).lower()
        return data

    def create(self, validated_data):
        visit = VisitAgenda.objects.filter(client__id=validated_data['client_id'], datetime=validated_data['datetime']).first()
        if visit:
            return visit
        visit = VisitAgenda.objects.create(**validated_data)
        visit.save()
        return visit

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            try:
                setattr(instance, attr, value)
            except:
                pass
        instance.save()
        return instance

class SubPlanSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False, default=uuid4)
    parent_plan_id = serializers.UUIDField()
    # visits = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = SubPlan
        fields = "__all__"

class PlanSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False, default=uuid4)
    employee = EmployeeSerializer()
    name = serializers.CharField(required=False)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    target = serializers.IntegerField(required=True)
    description = serializers.CharField(required=False)
    childs = SubPlanSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = "__all__"
