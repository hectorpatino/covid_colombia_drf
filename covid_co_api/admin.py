from django.contrib import admin
from covid_co_api.models import Gender, Possitive


# Register your models here.


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('type', )


@admin.register(Possitive)
class PossitiveAdmin(admin.ModelAdmin):
    list_filter = ('severity_status',)
    ordering = ('notification_date', 'web_report')
    search_fields = ('web_report', 'notification_date', 'age', 'severity_status')