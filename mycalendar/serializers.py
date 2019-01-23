from rest_framework import serializers
from mycalendarapp.models import *

# Serializers define the API representation.
class WorkshopEventSerializer(serializers.Serializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:event-detail", lookup_field = 'Event')

    class Meta:
        model = WorkshopEvent
        fields = ('url', 'event', 'room', 'gear')
