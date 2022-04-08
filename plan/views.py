from datetime import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from utils.renderers import JSONRenderer
from .models import Plan, SubPlan, VisitAgenda
from .serializers import PlanSerializer, SubPlanSerializer, VisitQuerySerializer, VisitSerializer

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

class VisitView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = VisitSerializer

    def get_queryset(self):
        data = VisitAgenda.objects.filter(plan__employee__id=self.request.user.id)
        return data

    def create(self, request):
        data = request.data
        is_many = isinstance(data, list)

        serializer = VisitSerializer(data=data, many=is_many)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)      
        
    def list(self, request, *args, **kwargs):
        serializer = VisitQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        qs = self.get_queryset()
        qs = qs.filter(**serializer.data)
        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)  

    def retrieve(self, request, pk=None, *args, **kwargs):
        qs = self.get_queryset().filter(id=pk).first()
        serializer = VisitSerializer(qs)

        return Response(serializer.data, status=status.HTTP_200_OK)  

    def partial_update(self, request, pk, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        qs = self.get_queryset().filter(id=pk).first()
        self.perform_destroy(qs)

        return Response(status=status.HTTP_204_NO_CONTENT)  
        