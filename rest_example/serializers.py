from django.contrib.auth import get_user_model
from django.conf import settings



from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import ValidationError


class LoginSerializer(AuthTokenSerializer):

    def validate(self, attrs):
        
        attrs = super(LoginSerializer, self).validate(attrs)
        
        return attrs


class TokenSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Token
        fields = ('key',)


class UserDetailsSerializer(serializers.ModelSerializer):

   
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'specialname', 'details')


