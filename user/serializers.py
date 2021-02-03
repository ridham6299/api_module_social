from base.email import send_email
from base.exceptions import BaseValidationError
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


    def update(self, instance, validated_data):
        _password = validated_data.pop("password", None)

        if _password:
            self.instance.set_password(_password)

        return super(UserSerializer, self).update(instance, validated_data)
