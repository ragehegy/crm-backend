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
    id = serializers.UUIDField(required=False, default=uuid4, write_only=True)
    details = ProductSerializer(source='product', required=False)
    feedback = serializers.CharField(required=False, default=0)
    notes = serializers.CharField(required=False, default='')

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

        # TODO: Filter by request.user.id
        # instance.update({
        #     'plan__parent_plan__employee__id': instance.pop('employee_id')
        # })
        return super(VisitQuerySerializer, self).to_representation(instance)

class SubPlanSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False, default=uuid4)

    class Meta:
        model = SubPlan
        exclude = ('parent_plan', 'employee', )

class VisitSerializer(serializers.ModelSerializer):
    plan = SubPlanSerializer(required=False)
    client = BusinessClientSerializer(required=False)
    products = VisitProductSerializer(many=True, required=False)
    logs = VisitLogSerializer(many=True, required=False)

    class Meta:
        model = VisitAgenda
        fields = "__all__"
    
    def create(self, validated_data):
        products = validated_data.pop('products', None)
        plan = validated_data.pop('plan', None)
        client = validated_data.pop('client', None)

        if not plan or not client:
            raise serializers.ValidationError('Plan and Client fields are required.')

        validated_data['plan_id'] = plan['id']
        validated_data['client_id'] = client['id']

        visit = VisitAgenda.objects.create(**validated_data)
        if products:
            VisitProduct.objects.bulk_create(
                [
                    VisitProduct(
                        visit=visit, 
                        product_id=product['id'],
                        feedback=product['feedback'],
                        notes=product['notes'],
                    )
                    for product in products]
            )
        return visit

    def update(self, instance, validated_data):
        products = validated_data.pop('products', None)
        if products:
            old = VisitProduct.objects.filter(visit_id=instance.id)
            old.delete()
            VisitProduct.objects.bulk_create(
                [
                    VisitProduct(
                        visit=instance, 
                        product_id=product['id'],
                        feedback=product.get('feedback', 0),
                        notes=product.get('notes', ""),
                    )
                    for product in products
                ]
            )
        for attr, value in validated_data.items(): 
            setattr(instance, attr, value)
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = data.get('status', None).upper()
        data['approval_status'] = data.get('approval_status', None).upper()
        data['type'] = data.get('type', None).upper()
        return data

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
