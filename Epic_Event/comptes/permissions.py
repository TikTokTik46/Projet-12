from rest_framework import permissions
from contrats import models
from évènements import models

class ComptesPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.user_profile == "SU":
                return False
            elif request.user.user_profile == "SA":
                return False
            elif request.user.user_profile == "GE":
                return True
            else:
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
                event_contract = models.Event.objects.filter(
                    support_contact=request.user
                )
                contract_client = models.Contrat.objects.filter(id__in=event_contract)
                return obj in models.Client.objects.filter(id__in=contract_client)
            elif request.user.user_profile == "SA":
                return request.user == obj.employee_contact
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
