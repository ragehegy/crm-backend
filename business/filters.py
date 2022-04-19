import django_filters

from .models import Business, BusinessClient

class BusinessFilter(django_filters.FilterSet):
    class Meta:
        model = Business
        fields = {
            'id': ['exact', ],
            'active': ['exact', ],
        }

class BusinessClientFilter(django_filters.FilterSet):
    class Meta:
        model = BusinessClient
        fields = {
            'client__name': ['contains', ],
        }