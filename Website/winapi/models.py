from __future__ import unicode_literals
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Dll(models.Model):
    name = models.CharField(max_length=100)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class API(models.Model):
    name = models.CharField(max_length=100)
    hash_value = models.CharField(max_length=64, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    dll = models.ForeignKey(Dll, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
