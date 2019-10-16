import re

from django.contrib.auth import password_validation
from rest_framework import serializers

from apps.users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    first_name = serializers.CharField(
        required=True,
        allow_blank=True,
    )
    last_name = serializers.CharField(
        required=True,
        allow_blank=True,
    )

    def create(self, validated_data):

        validated_data.pop("confirm_password")
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, data):

        self.check_valid_password(data)
        self.check_valid_email(data['email'])
        return data

    @staticmethod
    def check_valid_password(value):
        password = value.get('password')
        confirm_password = value.get('confirm_password')
        if not re.search(r"\d", password) or not re.search(r"[a-zA-Z]", password):
            raise serializers.ValidationError('The password must contain at letters and numbers')

        try:
            password_validation.validate_password(password=password)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(e.detail)

        if password != confirm_password:
            raise serializers.ValidationError("Password and Confirm Password fields must match.")

    @staticmethod
    def check_valid_email(value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email address already exists.')

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'password',
            'confirm_password',
        ]
