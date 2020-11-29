from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'product')


class UserSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'first_name', 'last_name',
            'birth_date', 'registration_date', 
            'order', 
        )
