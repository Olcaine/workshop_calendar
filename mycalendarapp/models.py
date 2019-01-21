# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from schedule.models import Event

class WorkshopEvent(models.Model):
    #animateur
    #salle
    #matos
    event = models.ForeignKey(Event)
