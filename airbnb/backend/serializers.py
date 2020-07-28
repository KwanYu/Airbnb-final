from rest_framework import serializers
from .models import Airbnb
from django.contrib.auth.models import User


class AirbnbSerializer(serializers.ModelSerializer):
    class meta:
        model = Airbnb
        fields = '_all_'
        extra_kwargs = {
                        'name': {'required': True},
                        'host_name': {'required': True}
                        }
