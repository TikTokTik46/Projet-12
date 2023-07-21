from rest_framework.response import Response
from comptes.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from comptes.models import User
from rest_framework.permissions import IsAuthenticated
from comptes.permissions import ComptesPermissions

class ComptesViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ComptesPermissions]

