from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models import User_Roles, Users, Airline_Companies, Countries, Flights
from ..serilizers import Flights_Serializer

@api_view(['GET','POST','DELETE','PUT'])
def flight(request,pk=-1):
    if request.method == 'GET':
        if int(pk) > -1:
            Flight = Flights.objects.filter(id=pk).first()
            serializer = Flights_Serializer(Flight, many=False)
            if Flight:
                return Response(serializer.data)
            else:
                return Response('Flight does not exist', status=status.HTTP_400_BAD_REQUEST)
        else:  # return all
            Flight = Flights.objects.all()
            serializer = Flights_Serializer(Flight, many=True)
            return Response(serializer.data)
    
    if request.method == 'POST': #method post add new row !!!! need to construct a result for POST DELETE and PUT!
        serializer = Flights_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE': #method Delete a row
        Flight = Flights.objects.filter(id=pk).first()
        if Flight:
            Flight.delete()
            return Response('Flight Deleted')
        return Response('Flight not found',status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT': #need to create all options for Put
        Flight = Flights.objects.filter(id=pk).first()
        serializer = Flights_Serializer(instance=Flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def flightByCountry(request,pk=-1):
    flights = Flights.get_flights_by_country(country_id = pk)
    serializer = Flights_Serializer(flights , many=True)
    if request.method == 'GET':
        return Response(serializer.data)


# class Flights(models.Model):
#     Airline_Company_Id = models.ForeignKey(Airline_Companies, on_delete=models.CASCADE, null=True)
#     Origin_Country_Id = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True, related_name='Origin_Country_Id')
#     Destination_Country_Id = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True, related_name='Destination_Country_Id')
#     Departure_Time = models.DateTimeField(null=True)
#     Landing_Time = models.DateTimeField(null=True)
#     Remaining_Tickets = IntegerField(max_value=1000,min_value=0)
