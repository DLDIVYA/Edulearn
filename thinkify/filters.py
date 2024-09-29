import django_filters

from .models import *

class ExamFilter(django_filters.FilterSet):
    class Meta:
        model = Exams
        fields = '__all__'