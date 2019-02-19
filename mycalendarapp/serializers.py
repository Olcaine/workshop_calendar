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
    room = RoomSerializer(many=True)
    equipment = EquipmentSerializer(many=True)

    class Meta:
        model = WorkshopEvent
        fields = ('event', 'room', 'equipment')

#       Error 500 (bdd) - probleme data avec room & equipment

#     def to_internal_value(self, data):
#         print data
#         try:
#             data['event'] = data['event']['room']['equipment']
#         except TypeError:
#             pass
#         return super(WorkshopEventSerializer, self).to_interval_value(data)
#
#     def to_representation(self, instance):
#         return ReadWorkshopEventSerializer(instance).data
#
# class ReadWorkshopEventSerializer(serializers.ModelSerializer):
#     event = WorkshopEventSerializer()
#
#     class Meta(EventSerializer.Meta):
#         pass

    # if "workshopevent" in request.data:
    #     request.data["workshopevent_id"] = request.data['workshopevent']
    #
    #     return super(WorkshopEventViewSet, self).create(request, *args, **kwargs)

    # def test_workshop_data(self):
    #
    # serializer = WorkshopEventSerializer(data=data)
    # serializer.is_valid(raise_exception=True)
    # serializer.validated_data
    # serializer.save()

        # return WorkshopEvent(**validated_data)

    def create(self, validated_data):

        event = Event.objects.create(start=validated_data['event']["start"],
                                     end=validated_data['event']["end"],
                                     title=validated_data['event']["title"],
                                     description=validated_data['event']["description"],
                                     calendar=validated_data['event']["calendar"])

        return WorkshopEvent.objects.create(event=event, room=validated_data["room"], equipment=validated_data["equipment"])
