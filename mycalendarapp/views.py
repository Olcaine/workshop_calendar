# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mycalendarapp.models import *
from mycalendar.serializers import *
from rest_framework import viewsets


class WorkshopEventViewSet(viewsets.ModelViewSet):
    queryset = WorkshopEvent.objects.all()
    serializer_class = WorkshopEventSerializer
    # filter_class = WorkshopEventFilter

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return ReadWorkshopEventSerializer
    #     else:
    #         return serializer_class
    #
    # def list(self, request, *args, **kwargs):
    #
    #     queryset = self.filter_queryset(self.get_queryset())

class WorkshopEventListView(ListView):
    model = WorkshopEvent

class WorkshopEventDetailView(DetailView):
    model = WorkshopEvent

class WorkshopEventCreateView(CreateView):
    model = WorkshopEvent

class WorkshopEventUpdateView(UpdateView):
    model = WorkshopEvent
    fields = "__all__"

    def get_success_url(self):
        return reverse("workshop_event_detail", args=[self.object.slug])

class WorkshopEventDeleteView(DeleteView):
    model = WorkshopEvent
    success_url = reverse_lazy("workshop_event_list")
