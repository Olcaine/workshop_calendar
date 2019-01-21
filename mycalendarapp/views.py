# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import WorkshopEvent

class WorkshopEventListView(ListView):
    model = WorkshopEvent

class WorkshopEventDetailView(DetailView):
    model = WorkshopEvent

class WorkshopEventCreateView(CreateView):
    model = WorkshopEvent

class WorkshopEventUpdateView(UpdateView):
    model = Event
    fields = "__all__"

    def get_success_url(self):
        return reverse("workshop_event_detail", args=[self.object.slug])

class WorkshopEventDeleteView(DeleteView):
    model = Event
    sucess_url = reverse_lazy("workshop_event_list")
