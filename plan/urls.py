from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlanView.as_view({'get': 'list', 'post': 'create'}), name='plans'),
    path('sub', views.PlanView.as_view({'get': 'retrieve'}), name='subplans'),
    path('visits', views.VisitView.as_view({'post': 'create', 'get': 'list'}), name='visits'),
    path('visits/<pk>', views.VisitView.as_view(
            {
                'get': 'retrieve', 
                'delete': 'destroy', 
                'patch': 'partial_update'
            }
        ), 
        name='visit'
    ),
    path('visits', views.VisitView.as_view({'post': 'create', 'get': 'list'}), name='visits'),
    path('aggregates/date', views.PlanAggregatesView.as_view({'get': 'list_by_date'}), name='aggregates_date'),
    path('aggregates/employees', views.PlanAggregatesView.as_view({'get': 'list_employees'}), name='aggregates_date'),
    path('aggregates', views.PlanAggregatesView.as_view(
            {
                'get': 'retrieve',
            }
        ), 
        name='aggregates'
    ),
    path('subplan', views.SubPlanView.as_view({'get': 'list'}), name='subplan'),
]