from django_filters import rest_framework as filters

from ruku.models import Forecast


class AdminForecastFilter(filters.FilterSet):
    start_date = filters.DateTimeFilter(field_name='arrivedtime',lookup_expr=('gte'),input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    end_date = filters.DateTimeFilter(field_name='arrivedtime',lookup_expr=('lte'),input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])

    class Meta:
        model = Forecast
        fields = ['product_name', 'logistic_code', 'owner',
                  'start_date',  'end_date']
