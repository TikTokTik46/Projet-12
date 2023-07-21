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

    def get_sales_contact_name(self, obj):
        return display_name(obj.sales_contact)

    def get_has_contracts(self, instance):
        return instance.contrat_set.exists()

class ContratMixin:

    def get_contrat_id(self, obj):
        return display_id(obj)

    def get_date_created(self, obj):
        return display_time(obj.date_created)

    def get_date_updated(self, obj):
        return display_time(obj.date_updated)

    def get_sales_contact_name(self, obj):
        return display_name(obj.sales_contact)

class ClientListSerializer(ModelSerializer, ClientMixin):

    client_id = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()
    has_contracts = serializers.SerializerMethodField()
    sales_contact_name = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['client_id','first_name','last_name',
                  'company_name','date_updated','sales_contact',
                  'sales_contact_name', 'has_contracts']
        read_only_fields = ['client_id']

class ClientDetailSerializer(ModelSerializer, ClientMixin):

    client_id = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()
    has_contracts = serializers.SerializerMethodField()
    sales_contact_name = serializers.SerializerMethodField()


    class Meta:
        model = Client
        fields = ['client_id','first_name','last_name', 'email','phone','mobile',
                  'company_name','date_created','date_updated','sales_contact',
                  'sales_contact_name','has_contracts']
        read_only_fields = ['client_id','sales_contact_name']

class ContratListSerializer(ModelSerializer, ContratMixin):

    contrat_id = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()
    sales_contact_name = serializers.SerializerMethodField()

    class Meta:
        model = Contrat

        fields = ['contrat_id', 'sales_contact','sales_contact_name', 'client',
                  'date_updated', 'status']
        read_only_fields = ['contrat_id','sales_contact_name']

class ContratDetailSerializer(ModelSerializer, ContratMixin):

    contrat_id = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()
    sales_contact_name = serializers.SerializerMethodField()

    class Meta:
        model = Contrat

        fields = ['contrat_id','sales_contact','sales_contact_name','client','date_created','date_updated',
                  'status','amount_in_euros','payment_due']
        read_only_fields = ['contrat_id','sales_contact_name']

    def to_internal_value(self, data):
        choice_fields = {'status': Contrat.CONTRAT_STATUS}
        choice_fields_validator(data, choice_fields)
        return super().to_internal_value(data)