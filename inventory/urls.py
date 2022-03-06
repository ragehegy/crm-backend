from django.urls import path

from . import views

urlpatterns = [
    path('lines', views.LinesView.as_view(), name='lines'),
    path('products', views.ProductsView.as_view(), name='products'),
]