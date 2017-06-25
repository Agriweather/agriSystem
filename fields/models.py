from django.db import models
from schemes.models import Scheme
from django.contrib.auth import get_user_model
User = get_user_model()

class Field(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    gps_longitude = models.DecimalField(max_digits=8, decimal_places=3)
    gps_latitude = models.DecimalField(max_digits=8, decimal_places=3)
    city = models.CharField(max_length=90)


class FieldLog(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    scheme = models.ForeignKey(Scheme, default=1)
    f01 = models.CharField(max_length=64, blank=True)
    f02 = models.CharField(max_length=64, blank=True)
    f03 = models.CharField(max_length=64, blank=True)
    f04 = models.CharField(max_length=64, blank=True)
    f05 = models.CharField(max_length=64, blank=True)
    f06 = models.CharField(max_length=64, blank=True)
    f07 = models.CharField(max_length=64, blank=True)
    f08 = models.CharField(max_length=64, blank=True)
    f09 = models.CharField(max_length=64, blank=True)
    f10 = models.CharField(max_length=64, blank=True)
    f11 = models.CharField(max_length=64, blank=True)
    f12 = models.CharField(max_length=64, blank=True)
    f13 = models.CharField(max_length=64, blank=True)
    f14 = models.CharField(max_length=64, blank=True)
    f15 = models.CharField(max_length=64, blank=True)
    f16 = models.CharField(max_length=64, blank=True)
    f17 = models.CharField(max_length=64, blank=True)
    f18 = models.CharField(max_length=64, blank=True)
    f19 = models.CharField(max_length=64, blank=True)
    f20 = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = 'fieldlog'
        verbose_name_plural = 'fieldlogs'
        ordering = ['-datetime']
