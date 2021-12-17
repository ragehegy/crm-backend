from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from crm.data import *

@api_view(["GET"])
def index(request):
    cols = {"data": [
      {
        "Header": 'Name',
        "columns": [
          {
            "Header": 'First Name',
            "accessor": 'firstName',
          },
          {
            "Header": 'Last Name',
            "accessor": 'lastName',
          },
        ],
      },
      {
        "Header": 'Info',
        "columns": [
          {
            "Header": 'Age',
            "accessor": 'age',
          },
          {
            "Header": 'Visits',
            "accessor": 'visits',
          },
          {
            "Header": 'Status',
            "accessor": 'status',
          },
          {
            "Header": 'Profile Progress',
            "accessor": 'progress',
          },
        ],
      },
    ]}
    data = JsonResponse(cols)
    return data
    


@api_view(["GET"])
def sales(request):

    return JsonResponse(
        sample_data
    )