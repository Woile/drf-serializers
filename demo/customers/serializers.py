from django.contrib.auth.models import User
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class OutputCustomerSerializer(serializers.Serializer):
    username = serializers.CharField()
