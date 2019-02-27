from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from mycalendarapp.models import *
from schedule.models import Event
# Serializers define the API representation.
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = "__all__"

class WorkshopEventSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    room = RoomSerializer(read_only=True, many=True)
    equipment = EquipmentSerializer(read_only=True, many=True)

    class Meta:
        model = WorkshopEvent
        fields = ('id', 'event', 'room', 'equipment')


    def create(self, validated_data):

        event = Event.objects.create(start=validated_data['event']["start"],
                                     end=validated_data['event']["end"],
                                     title=validated_data['event']["title"],
                                     description=validated_data['event']["description"],
                                     calendar=validated_data['event']["calendar"])
        workshop_event = WorkshopEvent.objects.create(event=event)
        for room_id in self.context['request'].data["room"]:
            workshop_event.room.add(Room.objects.get(id=room_id))
        for equipment_id in self.context['request'].data["equipment"]:
            workshop_event.equipment.add(Equipment.objects.get(id=equipment_id))
        return workshop_event
