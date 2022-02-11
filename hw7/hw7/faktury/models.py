# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Faktura(models.Model):
    kwota=models.IntegerField(null=True, blank=True)
    nazwa_kupujacego=models.CharField(max_length=255, null=True, blank=True)
    termin_platnosci=models.DateTimeField(null=True, blank=True)
    czy_oplacono=models.BooleanField(default=False)


# Create your models here.
