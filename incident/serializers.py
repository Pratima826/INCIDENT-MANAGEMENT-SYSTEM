from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from incident.models  import *
from rest_framework.serializers import SerializerMethodField

## define here serializers class

class SignUpUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password',
        )

class LoginUserSerializers(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)
    
    class Meta:
        model = User
        fields = (
            'email','password',
        )

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'created_date',
            'updated_date',
        )
class IncidentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = (
            'id',
            'incident_number',
            'reporter_name',
            'reported_date',
            'priority','incident_status',
            'created_at',
            'updated_at'
        )
