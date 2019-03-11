# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from schedule.models import Event
from django.contrib.auth.models import User
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('workshopevent-detail', args=[self.id])

from django.db.models.signals import post_delete
from django.dispatch import receiver


@receiver(post_delete, sender=WorkshopEvent)
def delete_event(sender, instance, **kwargs):
    instance.event.delete()
