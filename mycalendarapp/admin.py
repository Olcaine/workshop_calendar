# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import WorkshopEvent
from schedule.models import Event


admin.site.register(WorkshopEvent)
