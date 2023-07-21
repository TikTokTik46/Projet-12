from rest_framework import permissions
from contrats.models import Client, Contrat
from évènements.models import Event

class ComptesPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_profile == 'GE':
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' and obj.is_superuser:
            return False  # Interdit la suppression d'un superutilisateur
        return True

class ClientPermissions(permissions.BasePermission):
    # permissions list
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        else:
            if request.user.user_profile == "SU":
                return False
            elif request.user.user_profile == "SA":
                return True
            elif request.user.user_profile == "GE":
                return True
            else:
                return False

    # permission detail
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            if request.user.user_profile == "SU":
                queryset_clients = Client.objects.filter(
                    contrat__event__support_contact=request.user
                )
                return obj in queryset_clients
            elif request.user.user_profile == "SA":
                return request.user == obj.sales_contact
            elif request.user.user_profile == "GE":
                return True
            else:
                return False
        elif request.method == "POST":
            if request.user.user_profile == "SU":
                return False
            elif request.user.user_profile == "SA":
                return True
            elif request.user.user_profile == "GE":
                return True
            else:
                return False
        else:
            if request.user.user_profile == "SA":
                return request.user == obj.sales_contact
            elif request.user.user_profile == "SU":
                return False
            elif request.user.user_profile == "GE":
                return True
            else:
                return False


class ContratPermissions(permissions.BasePermission):
    # permissions list
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        else:
            if request.user.user_profile == "SU":
                return False
            elif request.user.user_profile == "SA":
                return True
            elif request.user.user_profile == "GE":
                return True
            else:
                return False

    # permission detail
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            if request.user.user_profile == "SU":
                return False
            elif request.user.user_profile == "SA":
                return True
            elif request.user.user_profile == "GE":
                return True
            else:
                return False
        else:
            if request.user.user_profile == "SA":
                return request.user == obj.sales_contact
            elif request.user.user_profile == "SU":
                return False
            elif request.user.user_profile == "GE":
                return True
            else:
                return False


class EventPermissions(permissions.BasePermission):
    # permissions list
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        else:
            if request.user.user_profile == "SU" and request.method == "PUT" :
                return True
            elif request.user.user_profile == "SA":
                return True
            elif request.user.user_profile == "GE":
                return True
            else:
                return False

    # permission detail
    def has_object_permission(self, request, view, obj):
        if request.user.user_profile == "SU":
            return request.method in ["GET","PUT"] and request.user == obj.support_contact
        elif request.user.user_profile == "SA":
            return obj in Event.objects.filter(
                contrat__sales_contact=request.user)
        elif request.user.user_profile == "GE":
            return True
        else:
            return False