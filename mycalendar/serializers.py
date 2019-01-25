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

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        event = Event.objects.create(start=validated_data["start"], end=validated_data["end"], description=validated_data["description"], creator=validated_data["creator"], color_event=validated_data["color_event"]
                                     ),
        WorkshopEvent.objects.create(event=event, room=validated_data["room"], gear=validated_data["gear"])
        return event
