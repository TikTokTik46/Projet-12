from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from évènements.models import Event
from contrats.models import Contrat, Client
from contrats.serializers import ContratDetailSerializer, ContratListSerializer,\
    ClientDetailSerializer, ClientListSerializer
from comptes.permissions import ClientPermissions, ContratPermissions

class ClientViewSet(ModelViewSet):

    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [IsAuthenticated, ClientPermissions]
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update']:
            # Utiliser le serializer de détail pour la création
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContratViewSet(ModelViewSet):

    serializer_class = ContratListSerializer
    detail_serializer_class = ContratDetailSerializer
    permission_classes = [IsAuthenticated, ContratPermissions]
    queryset = Contrat.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update']:
            # Utiliser le serializer de détail pour la création
            return self.detail_serializer_class
        return super().get_serializer_class()
