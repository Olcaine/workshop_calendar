# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from schedule.models import Event

class WorkshopEvent(models.Model):
    #animateur
    #salle
    #matos
    event = models.ForeignKey(Event)
    room = models.CharField(max_length=120, default="none")
    gear = models.CharField(max_length=100, blank=True)

def __str__(self):
    return ugettext('%(title)s: %(start)s - %(end)s') % {
        'title': self.title,
        'description': self.description,
        'start': date(self.start, django_settings.DATE_FORMAT),
        'end': date(self.end, django_settings.DATE_FORMAT),
        'color': self.color,
        }
