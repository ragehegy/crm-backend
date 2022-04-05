from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from utils.renderers import JSONRenderer
from .models import Plan, VisitAgenda
from .serializers import PlanSerializer, VisitQuerySerializer, VisitSerializer

class PlanView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = PlanSerializer

    def list(self, request):
        qs = Plan.objects.filter(has_parent=False)

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        data = request.data
        is_many = isinstance(data, list)

        serializer = VisitSerializer(data=data, many=is_many)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)      

class VisitView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = VisitSerializer

    def get_queryset(self):
        data = VisitAgenda.objects.filter(plan__parent_plan__employee=self.request.user)
        return data

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

    def create(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)   
        