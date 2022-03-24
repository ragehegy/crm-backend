from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from utils.renderers import JSONRenderer
from .serializers import LeaveRequestQuerySerializer, LeaveRequestSerializer, RequestSerializer, RequestQuerySerializer
from .models import Request, LeaveRequest


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