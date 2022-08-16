from dataclasses import dataclass
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models import User_Roles, Users, Airline_Companies, Countries, Flights, Customers
from ..serilizers import CustomerSerializer

@api_view(['GET','POST','DELETE','PUT'])
def customers(request,pk=-1):
    if request.method == 'GET':
        if int(pk) > -1:
            customer = Customers.objects.filter(id=pk).first()
            serializer = CustomerSerializer(customer, many=False)
            if customer:
                return Response(serializer.data)
            else:
                return Response('Customer does not exist', status=status.HTTP_400_BAD_REQUEST)
        else:
            customer = Customers.objects.all()
            serializer = CustomerSerializer(customer, many=True)
            return Response(serializer.data)

    if request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        customer = Customers.objects.filter(id=pk).first()
        if customer:
            customer.delete()
            return Response('Customer Deleted')
        return Response('Customer not found',status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        customer = Customers.objects.filter(id=pk).first()
        serializer = CustomerSerializer(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
# class Customers(models.Model):
#     First_Name = models.CharField(max_length=20)
#     Last_Name = models.CharField(max_length=30)
#     Address = models.CharField(max_length=30)
#     Phone_No = models.CharField(max_length=30, unique=True)
#     Credot_Card_No = models.CharField(max_length=30, unique=True)
#     User_Id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
#     def __str__(self):
#         return self.First_Name + self.Last_Name
