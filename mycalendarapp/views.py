# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy

from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView

class WorkshopEventViewSet(viewsets.ModelViewSet):
    queryset = WorkshopEvent.objects.all()
    serializer_class = WorkshopEventSerializer

class RoomAPIListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class EquipmentAPIListView(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
