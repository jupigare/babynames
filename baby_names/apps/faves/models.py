from __future__ import unicode_literals
from ..login.models import User
from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class Frequency(models.Model):
    state = models.CharField(max_length=2, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequency'

class Favorites(models.Model):
    frequency = models.ForeignKey(Frequency)
    user = models.ForeignKey(User)
    # rating = models.IntegerField(blank=True, null=True)