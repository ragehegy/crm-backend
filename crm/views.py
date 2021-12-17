from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from .data import *

@api_view(["GET"])
def index(request):
    data = JsonResponse(sample_events)
    return data
    


@api_view(["GET"])
def clients(request):

    return JsonResponse(
        sample_data
    )