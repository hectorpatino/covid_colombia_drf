from rest_framework import serializers
from rest_framework.utils.field_mapping import get_url_kwargs
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from covid_co_api.models import Possitive, City, Gender, \
    CaseLocation, SeverityStatus, Department
from rest_framework.reverse import reverse

class DepartmentForCityPossitiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'nombre',
            'cod_dane',
        )


class CitySerializerForPossitive(serializers.HyperlinkedModelSerializer):
    department = DepartmentForCityPossitiveSerializer(read_only=True)

    class Meta:
        model = City
        fields = (
            'nombre',
            'cod_dane',
            'department',
        )


class PossitiveCaseSerializer(serializers.HyperlinkedModelSerializer):
    nurse = serializers.SlugRelatedField(queryset=get_user_model().objects.all(),
                                         slug_field='username')
    city = CitySerializerForPossitive()
    gender = serializers.SlugRelatedField(queryset=Gender.objects.all(),
                                          slug_field='type')
    case_location = serializers.SlugRelatedField(queryset=CaseLocation.objects.all(),
                                                 slug_field='type')
    severity_status = serializers.SlugRelatedField(queryset=SeverityStatus.objects.all(),
                                                   slug_field='type')

    class Meta:
        model = Possitive
        fields = (
            'url',
            'web_report',
            'notification_date',
            'age',
            'symptoms_date',
            'nurse',
            'city',
            'gender',
            'case_location',
            'severity_status',
        )

