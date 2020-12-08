from django.urls import path
from covid_co_api import views

urlpatterns = [
    path(r'possitives/',
         views.PossiviteCasesList.as_view(),
         name=views.PossiviteCasesList.name),
    path(r'possitivies/<int:pk>',
         views.PossitiveCaseDetail.as_view(),
         name=views.PossitiveCaseDetail.name),

    path('departments/',
         views.DepartmentList.as_view(),
         name=views.DepartmentList.name),

    path('departments/<str:cod_dane>',
         views.DepartmentCaseDetail.as_view(),
         name=views.DepartmentCaseDetail.name),

    path('cities/',
         views.CityCaseList.as_view(),
         name=views.CityCaseList.name),
    path('cities/<str:cod_dane>',
         views.CityCaseDetail.as_view(),
         name=views.CityCaseDetail.name),

    path('age_city/<int:age>/<str:city>',
         views.PositiveAgeCityView.as_view(),
         name=views.PositiveAgeCityView.name),


    path(r'', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
