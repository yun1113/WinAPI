from __future__ import unicode_literals
from django.db import models


class Dll(models.Model):
    name = models.CharField(max_length=100, unique=True)
    winxp = models.BooleanField(default=False)
    win7 = models.BooleanField(default=False)
    win8 = models.BooleanField(default=False)
    win10 = models.BooleanField(default=False)
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


class MalwareAPICallExcutionTrace(models.Model):
    malware_name = models.CharField(max_length=100, blank=True, null=True)
    sha256 = models.CharField(max_length=100, blank=True, null=True)
    api = models.ManyToManyField(API)
    dll = models.ManyToManyField(Dll, blank=True)

    def __str__(self):
        return self.sha256


class MalwareAPICall(models.Model):
    malware_excution_trace = models.ForeignKey(MalwareAPICallExcutionTrace, blank=True, null=True)
    api = models.ForeignKey(API)
    dll = models.ForeignKey(Dll, blank=True)
    count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.malware_excution_trace
