from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models import Administrators
from ..serilizers import Administrators_Serializer


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def administrator(request, pk=-1):
    if request.method == 'GET':
        if int(pk) > -1:
            Administrator = Administrators.objects.filter(id=pk).first()
            serializer = Administrators_Serializer(Administrator, many=False)
            if Administrator:
                return Response(serializer.data)
            else:
                return Response('Administrator does not exist', status=status.HTTP_400_BAD_REQUEST)
        else:  # return all
            Administrator = Administrators.objects.all()
            serializer = Administrators_Serializer(Administrator, many=True)
            return Response(serializer.data)

    if request.method == 'POST': #method post add new row !!!! need to construct a result for POST DELETE and PUT!
        serializer = Administrators_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE': #method Delete a row
        Administrator = Administrators.objects.filter(id=pk).first()
        if Administrator:
            Administrator.delete()
            return Response('Administrator Deleted')
        return Response('Administrator not found',status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT': #need to create all options for Put
        Administrator = Administrators.objects.filter(id=pk).first()
        serializer = Administrators_Serializer(instance=Administrator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def about(req):
    return HttpResponse('<h1>about first</h1>')



# class Administrators(models.Model):
#     First_Name = models.CharField(max_length=30)
#     Last_Name = models.CharField(max_length=30)
#     User_Id = models.OneToOneField(Users, on_delete=models.CASCADE, unique=True)
