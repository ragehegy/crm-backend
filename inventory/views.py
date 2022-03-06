from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .renderers import UserJSONRenderer
from .serializers import LineSerializer, ProductSerializer
from .models import Line, Product


class LinesView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LineSerializer

    def get(self, request):
        qs = Line.objects.all()

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductsView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = ProductSerializer

    def get(self, request):
        qs = Product.objects.all()

        serializer = self.serializer_class(qs, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
