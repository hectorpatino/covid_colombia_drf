from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework import generics
from covid_co_api.custompagination import LimitOffsetPaginationWithUpperBound
from covid_co_api.models import Possitive, Department, City
from rest_framework.response import Response
from covid_co_api.serializers import (
    PossitiveCaseSerializer,
    DepartmentSerializer,
    CitySerializer,
)
from rest_framework.throttling import ScopedRateThrottle


class PossiviteCasesList(generics.ListCreateAPIView):
    name = 'possitive-list'
    queryset = Possitive.objects.all()
    serializer_class = PossitiveCaseSerializer
    throttle_classes = (ScopedRateThrottle,)
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )
    filter_fields = (
        'city',
        'gender',
        'case_location',
        'severity_status',
    )
    search_field = (
        'city',
    )
    ordering_fields = (
        'age',
    )
    pagination_class = LimitOffsetPaginationWithUpperBound


    def perform_create(self, serializer):
        serializer.save(nurse=self.request.user)


class PossitiveCaseDetail(generics.RetrieveAPIView):
    name = 'possitive-detail'
    queryset = Possitive.objects.all()
    serializer_class = PossitiveCaseSerializer


class DepartmentList(generics.ListAPIView):
    """
    Lists all departments in the country
    """
    name = 'department-list'
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCaseDetail(generics.RetrieveAPIView):
    """
    Retrieve department caracteristics
    """
    name = 'department-detail'
    lookup_field = 'cod_dane'
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class CityCaseList(generics.ListAPIView):
    name = 'city-list'
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_fields = (
        'nombre',
        'cod_dane',
        'department',
    )
    search_field = (
        'nombre',
        'cod_dane',
        'department',
    )
    ordering_fields = (
        'cod_dane',
    )


class CityCaseDetail(generics.RetrieveAPIView):
    name = 'city-detail'
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'cod_dane'


class PositiveAgeCityView(generics.ListAPIView):
    name = 'possitive-age-detail'
    serializer_class = PossitiveCaseSerializer

    def get_queryset(self):
        age = self.kwargs['age']
        city = self.kwargs['city']
        return Possitive.objects.filter(age=age, city__cod_dane=city)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'possitive-cases': reverse(PossiviteCasesList.name, request=request),
            'department-cases': reverse(DepartmentList.name, request=request),
            'cities-cases': reverse(CityCaseList.name, request=request),
        })