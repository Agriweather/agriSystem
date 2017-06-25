from django.db import models

class Scheme(models.Model):
    name = models.CharField(max_length=128, blank=False)
    descriptor = models.CharField(max_length=512, blank=True)

    class Meta:
        verbose_name = 'scheme'
        verbose_name_plural = 'schemes'
        ordering = ['-name']
