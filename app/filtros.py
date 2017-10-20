import django_filters
from app.models import *


class CdrFilter(django_filters.FilterSet):

	class Meta:
		model = BitCdr

		fields = {
		'src': ['lt', 'gt'],
		'calldate': ['exact', 'year__gt'],
		}
		filter_overrides = {
			models.CharField: {
			    'filter_class': django_filters.CharFilter,
			    'extra': lambda f: {
			        'lookup_expr': 'icontains',
			    },
			},
			models.BooleanField: {
			    'filter_class': django_filters.BooleanFilter,
			    'extra': lambda f: {
			        'widget': forms.CheckboxInput,
			    },
			},
		}