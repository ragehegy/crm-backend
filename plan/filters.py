import django_filters

from .models import VisitAgenda

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = VisitAgenda
        fields = {
            'id': ['exact', ],
            'plan__employee__id': ['exact', ],
            'status': ['exact', ],
            'type': ['exact', ],
        }
