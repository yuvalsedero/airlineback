from rest_framework import viewsets
from django.contrib.auth.models import User
from ..serilizers import Users_Serializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Users_Serializer

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.template import loader
# from ..models import User_Roles, Users
# from ..serilizers import Users_Serializer

# @api_view(['GET','POST','DELETE','PUT'])
# def users(request,pk=-1): # BUG Users serializer has a bug and cannot post or affect UserRole.. stuck to default "User"
#     if request.method == 'GET':
#         if int(pk) > -1:
#             User = Users.objects.filter(id=pk).first()
#             serializer = Users_Serializer(User, many=False)
#             if User:
#                 return Response(serializer.data)
#             else:
#                 return Response('User does not exist', status=status.HTTP_400_BAD_REQUEST)
#         else:  # return all
#             User = Users.objects.all()
#             serializer = Users_Serializer(User, many=True)
#             return Response(serializer.data)


#     if request.method == 'POST': #method post add new row !!!! need to construct a result for POST DELETE and PUT!
#         serializer = Users_Serializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE': #method Delete a row
#         User = Users.objects.filter(id=pk).first()
#         if User:
#             User.delete()
#             return Response('User Deleted')
#         return Response('User not found',status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PUT': #need to create all options for Put
#         User = Users.objects.filter(id=pk).first()
#         serializer = Users_Serializer(instance=User, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def about(req):
#     return HttpResponse('<h1>about first</h1>')



# #     Username = models.CharField(max_length=30, unique=True)
# #     Password = models.CharField(max_length=30)
# #     Email = models.CharField(max_length=50, unique=True)
# #     User_Role = models.CharField(max_length=30, unique=True, choices=User_Roles.choices)

#     #     UserRoles:
#     #     User = "User"
#     #     Flight_Company = "Flight_Company"
#     #     Administrator = "Administrator" 