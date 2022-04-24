from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from business.filters import BusinessClientFilter
from utils.renderers import JSONRenderer
from .serializers import BusinessClientSerializer, BusinessDistrictSerializer, BusinessDistrictsSerializer, DistrictBrickSerializer, LeaveRequestQuerySerializer, LeaveRequestSerializer, RequestSerializer, RequestQuerySerializer
from .models import BusinessClient, BusinessDistrict, DistrictBrick, Request, LeaveRequest


class RequestsView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = RequestSerializer

    def get(self, request):
        qs = RequestQuerySerializer(data=request.query_params)
        qs.is_valid(raise_exception=True)
        data = qs.data

        qs = Request.objects.filter(**data)

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class LeaveRequestsView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    serializer_class = LeaveRequestSerializer

    def get(self, request):
        qs = LeaveRequestQuerySerializer(data=request.query_params)
        qs.is_valid(raise_exception=True)
        data = qs.data

        qs = LeaveRequest.objects.filter(**data)

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BusinessClientsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    queryset = BusinessClient.objects.all()
    serializer_class = BusinessClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BusinessClientFilter
    
class BusinessDistrictsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    queryset = BusinessDistrict.objects.all()
    serializer_class = BusinessDistrictSerializer

class DistrictBricksView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    queryset = DistrictBrick.objects.all()
    serializer_class = DistrictBrickSerializer