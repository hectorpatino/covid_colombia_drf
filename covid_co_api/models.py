from django.db import models
# from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class Department(models.Model):
    nombre = models.CharField(max_length=100)
    cod_dane = models.CharField(max_length=50)
    # geom = models.MultiPolygonField(srid=4326, null=True)

    class Meta:
        ordering = ('cod_dane', )
        verbose_name = 'Department'
        verbose_name_plural = 'Deparments'

    def __str__(self):
        return self.nombre


class City(models.Model):
    nombre = models.CharField(max_length=50)
    department = models.ForeignKey(Department,
                                   related_name='cities',
                                   on_delete=models.CASCADE)
    cod_dane = models.CharField(max_length=50)
    # geom = models.MultiPolygonField(srid=4326, null=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.nombre} - {self.department}'


class CaseLocation(models.Model):
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = "CaseLocation"
        verbose_name_plural = "CaseLocations"

    def __str__(self):
        return self.type


class SeverityStatus(models.Model):
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = "SeverityStatus"
        verbose_name_plural = "SeverityStatus"

    def __str__(self):
        return self.type


class Gender(models.Model):
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = "Genders"

    def __str__(self):
        return self.type


class Possitive(models.Model):
    web_report = models.DateField()
    notification_date = models.DateField()
    age = models.IntegerField()
    symptoms_date = models.DateField(null=True)
    nurse = models.ForeignKey(get_user_model(),
                              related_name='Possitives_reported',
                              on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City,
                             related_name='possitives',
                             on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender,
                               related_name='possitives',
                               on_delete=models.CASCADE)
    case_location = models.ForeignKey(CaseLocation,
                                      related_name='possitives',
                                      on_delete=models.SET_NULL,
                                      null=True)
    severity_status = models.ForeignKey(SeverityStatus,
                                        related_name='possitives',
                                        on_delete=models.SET_NULL,
                                        null=True)

    class Meta:
        ordering = ('notification_date',)
        verbose_name = "Possitive"
        verbose_name_plural = "Possitives"

    def __str__(self):
        return f'{self.id} - {self.notification_date}'


class DeathDates(models.Model):
    possitive = models.OneToOneField(Possitive,
                                     related_name='possitive_deaths',
                                     on_delete=models.CASCADE)
    death_date = models.DateField()

    class Meta:
        verbose_name = "DeathDate"
        verbose_name_plural = "DeathDates"

    def __str__(self):
        return f'{self.possitive} - {self.death_date}'


class RecoveryDates(models.Model):
    possitive = models.OneToOneField(Possitive,
                                     related_name='possitive_recovery',
                                     on_delete=models.CASCADE)
    recovery_date = models.DateField()

    class Meta:
        verbose_name = "RecoveryDate"
        verbose_name_plural = "RecoveryDates"

    def __str__(self):
        return f'{self.possitive} - {self.recovery_date}'
