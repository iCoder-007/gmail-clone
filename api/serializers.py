from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import Mail

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        fields=[
            'first_name'
            'last_name'
            'username'
            'password'
        ]
        model=User
class SignInStautsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=[
            
            'token'
        ]
        model=User


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        fields=[
            'subject'
            'text'
            'to'
        ]
        model=Mail
class SMailSerializer(serializers.ModelSerializer):
    class Meta:
        fields=[
            'sno'
        ]
        model=Mail