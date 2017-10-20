import django_filters
from app.models import *
from django import forms


class CdrFilter(django_filters.FilterSet):

    calldate = django_filters.CharFilter()
    src = django_filters.CharFilter()
 
    class Meta:
        model = BitCdr
        fields = {
            'src': ['exact', ],
            'calldate': ['year', 'year__gt', 'year__lt', ]

        }


