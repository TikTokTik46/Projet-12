from rest_framework import serializers
from comptes.models import User
from Epic_Event.utils import choice_fields_validator

class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'password_confirmation', 'first_name', 'last_name', 'user_profile']
        extra_kwargs = {
            'password': {'write_only': True},
            'user_profile': {'required': True}
        }

    def to_internal_value(self, data):
        choice_fields = {'user_profile': User.USER_PROFILES}
        choice_fields_validator(data, choice_fields)
        return super().to_internal_value(data)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Un utilisateur avec cette adresse e-mail existe déjà.")
        return value

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
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

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)
        instance.user_profile = validated_data.get('user_profile',
                                                   instance.user_profile)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance

class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                "Le mot de passe actuel est incorrect.")
        return value