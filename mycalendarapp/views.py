# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy

from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView

class WorkshopEventViewSet(viewsets.ModelViewSet):
    queryset = WorkshopEvent.objects.all()
    serializer_class = WorkshopEventSerializer

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

class RoomAPIListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class EquipmentAPIListView(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
