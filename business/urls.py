from django.urls import path

from . import views

urlpatterns = [
    path('requests', views.RequestsView.as_view(), name='requests'),
    path('requests/leave', views.LeaveRequestsView.as_view(), name='leave_requests'),
    path('clients', views.BusinessClientsView.as_view({'get': 'list'}), name='business_clients'),
    path('districts', views.BusinessDistrictsView.as_view({'get': 'list'}), name='business_districts'),
    path('bricks', views.DistrictBricksView.as_view({'get': 'list'}), name='business_bricks'),
]