from rest_framework import serializers
from mycalendarapp.models import *

# Serializers define the API representation.
class WorkshopEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkshopEvent
        fields = ('url','event', 'room', 'gear')
        # lookup_field = 'workshopevent'
