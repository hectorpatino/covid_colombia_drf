from rest_framework import serializers
from covid_co_api.models import Department, Possitive


class DepartmentSerializer(serializers.ModelSerializer):
    cases = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='department-detail',
        lookup_field='cod_dane',
    )

    class Meta:
        model = Department
        fields = (
            'nombre',
            'url',
            'cod_dane',
            'cases',
        )

    def get_cases(self, obj):
        #
        # return Possitive.objects.filter(city__department__cod_dane=obj.cod_dane).count()
        amount = []
        department = Department.objects.get(cod_dane=obj.cod_dane)
        amount = [city.possitives.count() for city in department.cities.all() if city.possitives.count() > 0]
        return sum(amount)
