# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from schedule.models import Event
from django.contrib.auth.models import User

class Room(models.Model):
    location = models.CharField(max_length=150)

    def __unicode__(self):
        return self.location

class Equipment(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

# class Animator(models.Model):
#    user = models.ForeignKey(User)

class WorkshopEvent(models.Model):

    event = models.ForeignKey(Event)
    room = models.ManyToManyField(Room)
    equipment = models.ManyToManyField(Equipment)

    def __unicode__(self):
        return self.event.title

    # def __str_(self):
    #     return ugettext('%(title)s: %(start)s - %(end)s') % {
    #         'title': self.title,
    #         'description': self.description,
    #         'start': date(self.start, django_settings.DATE_FORMAT),
    #         'end': date(self.end, django_settings.DATE_FORMAT),
    #         'color': self.color,
    #         'room': self.room,
    #         'equipment': self.equipment,
    #         'user': self.user,
    #     }
