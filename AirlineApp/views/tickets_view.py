from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models import User_Roles, Users, Airline_Companies, Tickets
from ..serilizers import Tickets_Serializer


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def tickets(request, pk=-1):
    if request.method == 'GET':
        if int(pk) > -1:
            Ticket = Tickets.objects.filter(id=pk).first()
            serializer = Tickets_Serializer(Ticket, many=False)
            if Ticket:
                return Response(serializer.data)
            else:
                return Response('Ticket does not exist', status=status.HTTP_400_BAD_REQUEST)
        else:  # return all
            Ticket = Tickets.objects.all()
            serializer = Tickets_Serializer(Ticket, many=True)
            return Response(serializer.data)

    if request.method == 'POST': #method post add new row !!!! need to construct a result for POST DELETE and PUT!
        serializer = Tickets_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE': #method Delete a row
        Ticket = Tickets.objects.filter(id=pk).first()
        if Ticket:
            Ticket.delete()
            return Response('Ticket Deleted')
        return Response('Ticket not found',status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT': #need to create all options for Put
        Ticket = Tickets.objects.filter(id=pk).first()
        serializer = Tickets_Serializer(instance=Ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def about(req):
    return HttpResponse('<h1>about first</h1>')



# class Tickets(models.Model):
#     Flight_Id = models.OneToOneField(Flights, on_delete=models.CASCADE, null=True, unique=True)
#     Customer_Id = models.OneToOneField(Customers, on_delete=models.CASCADE, null=True, unique=True)