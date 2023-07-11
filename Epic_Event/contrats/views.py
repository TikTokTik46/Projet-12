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
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update']:
            # Utiliser le serializer de détail pour la création
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.method == "GET":
            if self.request.user.user_profile == "SU":
                contracts = Event.objects.filter(
                    support_contact=self.request.user
                )
                clients = Contrat.objects.filter(id__in=contracts)
                return queryset.filter(id__in=clients)
            elif self.request.user.user_profile == "SA":
                return queryset.filter(employee_contact=self.request.user)
            elif self.request.user.user_profile == "GE":
                return queryset
            else:
                return queryset
        else:
            return queryset

class ContratViewSet(ModelViewSet):

    serializer_class = ContratListSerializer
    detail_serializer_class = ContratDetailSerializer
    queryset = Contrat.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update']:
            # Utiliser le serializer de détail pour la création
            return self.detail_serializer_class
        return super().get_serializer_class()