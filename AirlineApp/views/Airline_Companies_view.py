from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models import User_Roles, Users, Airline_Companies, Countries
from ..serilizers import Airline_Companies_Serializer

@api_view(['GET','POST','DELETE','PUT'])
def airline_Companies(request,pk=-1):
    if request.method == 'GET':
        if int(pk) > -1:
            Airline_Company= Airline_Companies.objects.filter(id=pk).first()
            serializer = Airline_Companies_Serializer(Airline_Company, many=False)
            if Airline_Company:
                return Response(serializer.data)
            else:
                return Response('Airline company does not exist', status=status.HTTP_400_BAD_REQUEST)
        else: # return all
            Airline_Company = Airline_Companies.objects.all()
            serializer = Airline_Companies_Serializer(Airline_Company, many=True)
            return Response(serializer.data)

    if request.method == 'POST': #method post add new row !!!! need to construct a result for POST DELETE and PUT!
        serializer = Airline_Companies_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE': #method Delete a row
        Airline_Company = Airline_Companies.objects.filter(id=pk).first()
        if Airline_Company:
            Airline_Company.delete()
            return Response('Airline company Deleted')
        return Response('Airline company not found',status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT': #need to create all options for Put
        Airline_Company = Airline_Companies.objects.filter(id=pk).first()
        serializer = Airline_Companies_Serializer(instance=Airline_Company, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

def about(req):
    return HttpResponse('<h1>about first</h1>')



# class Airline_Companies(models.Model):
#     Name = models.CharField(max_length=30, unique=True)
#     Country_Id = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
#     User_Id = models.OneToOneField(Users, unique=True, on_delete=models.CASCADE, null=True)