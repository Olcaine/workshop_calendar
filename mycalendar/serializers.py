from rest_framework import serializers
from mycalendarapp.models import *
from schedule.models import Event
# Serializers define the API representation.
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class WorkshopEventSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    class Meta:
        model = WorkshopEvent
        fields = ('event', 'room', 'gear')
