from datetime import datetime
from django.db.models import Count, F, functions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from plan.filters import EmployeeFilter
from utils.renderers import JSONRenderer
from business.models import *
from .models import Plan, SubPlan, VisitAgenda
from .serializers import AggregateSerializer, EmployeeVisitsSerializer, PlanSerializer, SubPlanSerializer, SubPlanSummarySerializer, VisitQuerySerializer, VisitSerializer

class PlanView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = PlanSerializer

    def list(self, request):
        qs = Plan.objects.filter(has_parent=False, employee=self.request.user)

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        data = request.data
        is_many = isinstance(data, list)

        serializer = VisitSerializer(data=data, many=is_many)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)   
        
    def retrieve(self, request, *args, **kwargs):
        qs = SubPlan.objects.filter(start_date__month=datetime.now().month+1).first()
        serializer = SubPlanSerializer(qs)

        return Response(serializer.data, status=status.HTTP_200_OK)  

class SubPlanView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = SubPlanSummarySerializer

    def get_queryset(self):
        data = SubPlan.objects.filter(employee__id=self.request.user.id)
        return data

    def list(self, request):
        qs = SubPlan.objects.filter(employee=self.request.user)

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
class VisitView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = VisitSerializer
    queryset = VisitAgenda.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter

    def get_queryset(self):
        return self.queryset.filter(plan__employee__id=self.request.user.id)

    def create(self, request):
        data = request.data
        is_many = isinstance(data, list)

        serializer = VisitSerializer(data=data, many=is_many)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)      

    def destroy(self, request, pk=None, *args, **kwargs):
        qs = self.get_queryset().filter(id=pk).first()
        self.perform_destroy(qs)

        return Response(status=status.HTTP_204_NO_CONTENT)  
        
class PlanAggregatesView(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = AggregateSerializer
    queryset = VisitAgenda.objects.all()

    def get_queryset(self):
        return self.queryset.filter(plan__employee__id=self.request.user.id)
    
    def retrieve(self, request, *args, **kwargs):
        params = request.query_params
        qs = self.get_queryset().order_by(params['field']).\
            values(params['field']).\
                annotate(
                    value=F(params['field']), 
                    count=Count(params['field'])
                ).\
                filter(count__gt=0, plan__employee__id=self.request.user.id).all().\
                    values('value', 'count')

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)  

    def list_by_date(self, request):
        qs = self.get_queryset().order_by('datetime').\
            values('datetime').\
                annotate(
                    value=functions.TruncDate('datetime'), 
                    count=Count('datetime')
                ).filter(count__gt=0, plan__employee__id=self.request.user.id).all().\
                    values('value', 'count')

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)  

    def list_employees(self, request):
        qs = Employee.objects.filter(id=request.user.id)
        serializer = EmployeeVisitsSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
