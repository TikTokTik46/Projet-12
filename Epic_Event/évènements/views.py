from rest_framework.viewsets import ModelViewSet
from évènements.models import Event
from évènements.serializers import EventDetailSerializer, EventListSerializer
from rest_framework.permissions import IsAuthenticated
from comptes.permissions import EventPermissions


class EventViewSet(ModelViewSet):

    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated, EventPermissions]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update']:
            # Utiliser le serializer de détail pour la création
            return self.detail_serializer_class
        return super().get_serializer_class()