import django_filters
from app.models import *


class CdrFilter(django_filters.FilterSet):

    calldate = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BitCdr
        fields = {
            'src': ['exact', ],
            'calldate': ['year', 'year__gt', 'year__lt', ],
        }


