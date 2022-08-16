from rest_framework import serializers
from .models import Customers
from django.contrib.auth.models import User
from .models import Airline_Companies, Countries, User_Roles, Users, Flights, Customers, Tickets, Administrators
from rest_framework.authtoken.models import Token
class CustomerSerializer(serializers.ModelSerializer):
    # User_Id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Customers
        fields = '__all__'
        
class Airline_Companies_Serializer(serializers.ModelSerializer):
    # User_Id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Airline_Companies
        fields = '__all__'

class Countries_Serializer(serializers.ModelSerializer):
    # User_Id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Countries
        fields = '__all__'

class Users_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class Flights_Serializer(serializers.ModelSerializer):
    # User_Id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Flights
        fields = '__all__'

class Tickets_Serializer(serializers.ModelSerializer):
    # User_Id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tickets
        fields = '__all__'

class Administrators_Serializer(serializers.ModelSerializer):
    # User_Id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Administrators
        fields = '__all__'
