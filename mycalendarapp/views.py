# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy

from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView

class WorkshopEventViewSet(viewsets.ModelViewSet):
    queryset = WorkshopEvent.objects.all()
    serializer_class = WorkshopEventSerializer

    def get_queryset(self):
        calendar_id = self.request.query_params.get("calendar_id", None)
        if calendar_id:
            return self.queryset.filter(event__calendar__id=calendar_id)
        return self.queryset

class RoomAPIListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class EquipmentAPIListView(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
