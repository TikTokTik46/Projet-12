from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from models import Event
from ..Epic_Event.utils import display_time, display_name, \
    display_id, choice_fields_validator

class EventMixin:

    def get_event_id(self, obj):
        return display_id(obj)

    def get_date_created(self, obj):
        return display_time(obj.date_created)

    def get_date_updated(self, obj):
        return display_time(obj.date_updated)

    def get_support_contact(self, obj):
        return display_name(obj.support_contact)

    def get_event_status(self, obj):
        return obj.get_event_status_display()

class EventListSerializer(ModelSerializer, EventMixin):

    event_id = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['event_id','date_updated','attendees',
                  'event_date','contrat','event_status']
        read_only_fields = ['event_id']

    def to_internal_value(self, data):
        choice_fields = {'client_type': Event.EVENT_STATUS}
        choice_fields_validator(data, choice_fields)
        return super().to_internal_value(data)

class EventDetailSerializer(ModelSerializer, EventMixin):

    event_id = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()
    support_contact = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['event_id','contrat','date_created','date_updated',
                  'support_contact','event_status','attendees',
                  'event_date','notes']
        read_only_fields = ['event_id']

    def to_internal_value(self, data):
        choice_fields = {'client_type': Event.EVENT_STATUS}
        choice_fields_validator(data, choice_fields)
        return super().to_internal_value(data)