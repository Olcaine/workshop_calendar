# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mycalendarapp.models import *
from mycalendar.serializers import *
from rest_framework import viewsets


class WorkshopEventViewSet(viewsets.ModelViewSet):
    queryset = WorkshopEvent.objects.all()
    serializer_class = WorkshopEventSerializer
