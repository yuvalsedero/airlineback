
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from django.contrib.auth.models import User
from rest_framework.authtoken.views import obtain_auth_token
@api_view(['POST'])
def login(request):
        if request.data:
            found_user= User.objects.filter(username=request.data.get("username")).first()
            if not found_user:
                return HttpResponse("user not found", status=status.HTTP_404_NOT_FOUND  )
            if not found_user.check_password(request.data.get("password")):
                return HttpResponse("user not found", status=status.HTTP_404_NOT_FOUND  )
            return HttpResponse({obtain_auth_token})