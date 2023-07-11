from rest_framework.viewsets import ModelViewSet
from évènements.models import Event
from évènements.serializers import EventDetailSerializer, EventListSerializer


class EventViewSet(ModelViewSet):

    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update']:
            # Utiliser le serializer de détail pour la création
            return self.detail_serializer_class
        return super().get_serializer_class()