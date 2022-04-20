import django_filters

from .models import VisitAgenda

class VisitAgendaFilter(django_filters.FilterSet):
    client__client__specialties = django_filters.CharFilter(method='client__client__specialties__in')

    def client__client__specialties__in(self, queryset, value, *args, **kwargs):
        try:
            if args:
                ids = args[0].split(',')
                queryset = queryset.filter(client__client__specialties__specialty__en_name__in=ids)
        except ValueError:
            pass
        return queryset

    class Meta:
        model = VisitAgenda
        fields = {
            'id': ['exact', ],
            'approval_status': ['exact', 'in'],
            'status': ['exact', 'in'],
            'type': ['exact', 'in'],
            'datetime': ['exact', 'range'],

            'client__client__id': ['exact', ],
            'client__client__type': ['exact', 'in'],
            'client__client__client_class': ['exact', 'in'],

            'plan__id': ['exact', ],
            'plan__name': ['contains', ],
            'plan__employee__id': ['exact', 'in'],
            'plan__employee__first_name': ['contains', ],
            'plan__employee__last_name': ['contains', ],
            'plan__employee__district__district__city__id': ['in', ], # District
            'plan__employee__district__district__id': ['in', ], # Brick

            'products__product__id': ['in'],
            'products__product__line__id': ['in'],

        }
