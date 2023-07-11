from rest_framework import serializers
from comptes.models import User
from Epic_Event.utils import choice_fields_validator

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True,
                                                  required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    user_profile = serializers.CharField(required=True)

    def to_internal_value(self, data):
        choice_fields = {'user_profile': User.USER_PROFILES}
        choice_fields_validator(data, choice_fields)
        return super().to_internal_value(data)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Un utilisateur avec cette adresse e-mail existe déjà.")
        return value

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(
                "Les mots de passe ne correspondent pas.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_profile=validated_data['user_profile']
        )
        return user

