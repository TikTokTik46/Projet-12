from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from contrats.models import Client, Contrat
from comptes.models import User
from Epic_Event.utils import display_time, display_name, \
    display_id, choice_fields_validator

class ClientMixin:

    def get_client_id(self, obj):
        return display_id(obj)

    def get_date_created(self, obj):
        return display_time(obj.date_created)

    def get_date_updated(self, obj):
        return display_time(obj.date_updated)

    def get_sales_contact(self, obj):
        return display_name(obj.sales_contact)

    def get_client_type(self, obj):
        return obj.get_client_type_display()

class ContratMixin:

    def get_contrat_id(self, obj):
        return display_id(obj)

    def get_date_created(self, obj):
        return display_time(obj.date_created)

    def get_date_updated(self, obj):
        return display_time(obj.date_updated)

class ClientListSerializer(ModelSerializer, ClientMixin):

    client_id = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()
    client_type = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['client_id','first_name','last_name',
                  'company_name','date_updated','client_type']
        read_only_fields = ['client_id']

class ClientDetailSerializer(ModelSerializer, ClientMixin):

    client_id = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()


    class Meta:
        model = Client
        fields = ['client_id','first_name','last_name', 'email','phone','mobile',
                  'company_name','date_created','date_updated',
                  'sales_contact','client_type']
        read_only_fields = ['client_id']

    def to_internal_value(self, data):
        choice_fields = {'client_type': Client.CLIENT_TYPE}
        choice_fields_validator(data, choice_fields)
        return super().to_internal_value(data)


class ContratListSerializer(ModelSerializer, ContratMixin):

    contrat_id = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()

    class Meta:
        model = Contrat

        fields = ['contrat_id', 'sales_contact', 'client',
                  'date_updated', 'status', 'amount']
        read_only_fields = ['contrat_id']

class ContratDetailSerializer(ModelSerializer, ContratMixin):

    contrat_id = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()

    class Meta:
        model = Contrat

        fields = ['contrat_id','sales_contact','client','date_created','date_updated',
                  'status','amount','payment_due']
        read_only_fields = ['contrat_id']