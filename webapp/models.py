# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Counter(models.Model):
    count = models.IntegerField(default=0)

    @classmethod
    def Get(self):
        return Counter.objects.get_or_create(id=1)[0]

    @classmethod
    def Increment(self):
        counter = Counter.Get()
        counter.count += 1
        counter.save()
