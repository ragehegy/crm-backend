from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlanView.as_view({'get': 'list', 'post': 'create'}), name='plans'),
    path('', views.PlanView.as_view({'get': 'retrieve'}), name='plans'),
    path('visits', views.VisitView.as_view({'get': 'list'}), name='visits'),
    path('visits/<pk>', views.VisitView.as_view({'get': 'retrieve'}), name='visit'),
    # path('', views.PlanView.as_view({'post': 'create'}), name='plans'),
]