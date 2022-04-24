from uuid import uuid4

from django.db import models
from rest_framework import serializers

from business.models import Employee
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
    datetime = serializers.DateTimeField(required=False)
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
                        product_id=product['product']['id'],
                        feedback=product['feedback'],
                        notes=product['notes'],
                    )
                    for product in products]
            )
        return visit

    def update(self, instance, validated_data):
        products = validated_data.pop('products', None)
        plan = validated_data.pop('plan', None)
        client = validated_data.pop('client', None)
        logs = validated_data.pop('logs', None)

        instance.__dict__.update(**validated_data)
        instance.save()

        validated_data['plan_id'] = plan['id']
        validated_data['client_id'] = client['id']

        if products:
            old = VisitProduct.objects.filter(visit_id=instance.id)
            old.delete()
            VisitProduct.objects.bulk_create(
                [
                    VisitProduct(
                        visit=instance, 
                        product_id=product['product']['id'],
                        feedback=product.get('feedback', 0),
                        notes=product.get('notes', ""),
                    )
                    for product in products
                ]
            )

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

class AggregateSerializer(serializers.Serializer):
    value = serializers.CharField(required=True)
    count = serializers.FloatField()

class SubPlanSummarySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    employee = EmployeeSerializer()
    total_visits = serializers.IntegerField(read_only=True, source='visits.count')
    clients = BusinessClientSerializer(many=True, source='plan_clients')

    class Meta:
        model = SubPlan

class EmployeeVisitsSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    district = serializers.CharField(source='city')
    visits_details = VisitSerializer(many=True, source='visits.all')

    visits_total = serializers.IntegerField(source='visits.count')
    visits_coverage = serializers.SerializerMethodField()
    visits_rate = serializers.SerializerMethodField()
    working_days = serializers.IntegerField(source='month_working_days')
    top_product = serializers.SerializerMethodField()
    top_client = serializers.SerializerMethodField()
    top_tier = serializers.SerializerMethodField()
    avg_feedback = serializers.SerializerMethodField()

    def get_avg_feedback(self, obj):
        return obj.visits.aggregate(models.Avg('logs__feedback')).get('logs__feedback__avg', 0)

    def get_visits_coverage(self, obj):
        return obj.visits.filter(logs__status='CLOSED').count()

    def get_visits_rate(self, obj):
        return self.get_visits_coverage(obj)/obj.visits.count()

    def get_top__field(self, obj, field):
        return obj.visits.\
            values(field).\
                annotate(
                    value=models.F(field),
                    count=models.Count(field)
                ).\
                filter(count__gt=0).all().\
                    values('value', 'count').order_by('-count').first()

    def get_top_product(self, obj):
        return self.get_top__field(obj, 'products__product__name')

    def get_top_client(self, obj):
        return self.get_top__field(obj, 'client__client__type')

    def get_top_tier(self, obj):
        return self.get_top__field(obj, 'client__client__client_class')
    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'phone',
            'visits_details',
            'visits_total',
            'visits_coverage',
            'visits_rate',
            'working_days',
            'top_product',
            'top_client',
            'top_tier',
            'avg_feedback',
        )