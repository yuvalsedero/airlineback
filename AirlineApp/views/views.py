import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models import Airline_Companies, Countries, Users, Flights, Customers

# Create your views here.
def get_customer_by_username(request):
   Customer = Customers.get_customer_by_username('mor')
   template = loader.get_template('base.html')
#    context={
#        "myusers" : myusers.__dict__
#    }
   return HttpResponse(f"<h1>users named mor:</h1>")

def get_airline_by_username(request, Username):
    airline = Airline_Companies.get_airline_by_username(Username)
    return HttpResponse(f"<h1>users named mor:</h1>")

def get_user(request, username):
    user = Users.get_user_by_username(username)
    return HttpResponse(f"<h1>users named mor:</h1>")

def get_flights_by_parameters(request,origin_country_id,destination_country_id, startdate):
    flight = Flights.objects.filter(Origin_Country_Id = origin_country_id , Destination_Country_Id = destination_country_id, Departure_Time__range = (datetime.datetime(startdate), datetime.datetime(startdate) + datetime.timedelta(days=1))).first()
    return HttpResponse(f"<h1>users named mor:</h1>")

def about(req):
    return HttpResponse('<h1>about first</h1>')

def index(request):
    template = loader.get_template('index.html')
    context = {
       'Airline_Companies': Airline_Companies.objects.all()
    }
    return render(request, "index.html", context)

def addform(request):
    return render(request, "add.html")

def add(request):
    s = Countries(Name=request.POST["Name"])
    s.save()
    return HttpResponse("data added<a href='/AirlineApp/showall'>showall</a>")

def get_all_object(res, model):
    return JsonResponse(list(model.objects.all().values()), safe=False)

