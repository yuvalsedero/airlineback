from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models import User_Roles, Users, Airline_Companies, Countries
from ..serilizers import Countries_Serializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def countries(request, pk=-1):
    if request.method == 'GET':
        if int(pk) > -1:
            Country = Countries.objects.filter(id=pk).first()
            serializer = Countries_Serializer(Country, many=False)
            if Country:
                return Response(serializer.data)
            else:
                return Response('Country does not exist', status=status.HTTP_400_BAD_REQUEST)
        else:  # return all
            Country = Countries.objects.all()
            serializer = Countries_Serializer(Country, many=True)
            return Response(serializer.data)

    if request.method == 'POST': #method post add new row !!!! need to construct a result for POST DELETE and PUT!
        serializer = Countries_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE': #method Delete a row
        Country = Countries.objects.filter(id=pk).first()
        if Country:
            Country.delete()
            return Response('Country Deleted')
        return Response('Country not found',status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT': #need to create all options for Put
        Country = Countries.objects.filter(id=pk).first()
        serializer = Countries_Serializer(instance=Country, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

def about(req):
    return HttpResponse('<h1>about first</h1>')



# class Countries(models.Model):
#     Name = models.CharField(max_length=30, unique=True)