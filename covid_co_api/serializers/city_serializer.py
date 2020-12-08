from rest_framework import serializers
from covid_co_api.models import Department, City


class CitySerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.SlugRelatedField(queryset=Department.objects.all(),
                                              slug_field='nombre')
    cases = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name='city-detail',
        lookup_field='cod_dane')

    class Meta:
        model = City
        fields = (
            'url',
            'nombre',
            'cod_dane',
            'department',
            'cases',
        )

    def get_cases(self, obj):
        return City.objects.get(cod_dane=obj.cod_dane).possitives.count()