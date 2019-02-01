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
        fields = ('event', 'room', 'equipment')

    def create(self, validated_data):
        print validated_data
        event = Event.objects.create(start=validated_data['event']["start"],
                                     end=validated_data['event']["end"],
                                     title=validated_data['event']["title"],
                                     description=validated_data['event']["description"],
                                     calendar=validated_data['event']["calendar"])

        return WorkshopEvent.objects.create(event=event, room=validated_data["room"], equipment=validated_data["equipment"])
