# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy

from rest_framework import viewsets
from .models import *
from .serializers import *


class WorkshopEventViewSet(viewsets.ModelViewSet):
    queryset = WorkshopEvent.objects.all()
    serializer_class = WorkshopEventSerializer
