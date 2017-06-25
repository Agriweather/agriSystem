from django.db import models
from django_extensions.db.fields import (
        CreationDateTimeField, ModificationDateTimeField)

class FieldLog(models.Model):
    log_time = CreationDateTimeField()
    sensor = models.CharField(max_length=60)
    payload = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'fieldlog'
        verbose_name_plural = 'fieldlogs'
        ordering = ['-log_time']

