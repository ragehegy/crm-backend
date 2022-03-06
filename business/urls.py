from django.urls import path

from . import views

urlpatterns = [
    path('requests', views.RequestsView.as_view(), name='requests'),
    path('requests/leave', views.LeaveRequestsView.as_view(), name='leave_requests'),
]