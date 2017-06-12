from __future__ import unicode_literals
from django.db import models


class Dll(models.Model):
    name = models.CharField(max_length=100, unique=True)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class API(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hash_value = models.CharField(max_length=64, blank=True, null=True)
    dll = models.ManyToManyField(Dll, blank=True)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
