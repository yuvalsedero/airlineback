import datetime
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User
# Create your models here.
class Countries(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='images/', max_length=100, default='static/images/tamplates/image.jpg')
    # add a field for country flag for each country  (ImageField)
    def __str__(self):
     	return self.Name 

class User_Roles(models.TextChoices):
    User = "User"
    Flight_Company = "Flight_Company"
    Administrator = "Administrator" 

class Users(models.Model):
    Username = models.CharField(max_length=30, unique=True)
    Password = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50, unique=True)
    UserRole = models.CharField(max_length=30, choices=User_Roles.choices)
     # add a field for thumbnail img for each user (ImageField)
    def __str__(self):
        return self.Username 
    def get_user_by_username(username):
        user = Users.objects.filter(Username=username).first()
        return user

class Airline_Companies(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    Country_Id = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
    User_Id = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.Name 
    
    def get_airline_by_username(Username):
        airline = Airline_Companies.objects.filter(User_Id__Username=Username).first()
        return airline

class Flights(models.Model):
    Airline_Company_Id = models.ForeignKey(Airline_Companies, on_delete=models.CASCADE, null=True)
    Origin_Country_Id = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True, related_name='Origin_Country_Id')
    Destination_Country_Id = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True, related_name='Destination_Country_Id')
    Departure_Time = models.DateTimeField(null=True, default=datetime.datetime.now)
    Landing_Time = models.DateTimeField(null=True, default=datetime.datetime.now)
    Remaining_Tickets = models.IntegerField(default=0)
    def __str__(self):
        return self.Origin_Country_Id.__str__() + ' to ' + self.Destination_Country_Id.__str__() + ' with ' + self.Airline_Company_Id.__str__()

    def get_flights_by_parameters(origin_country_id: int, destination_country_id: int, startdate: datetime.datetime):
        flights = Flights.objects.filter(Origin_Country_Id = origin_country_id , Destination_Country_Id = destination_country_id, Departure_Time__range = (startdate, startdate + datetime.timedelta(days=1))).all()
        return flights
    
    def get_flights_by_airline_id(airline_id):
        flights = Flights.objects.filter(Airline_Company_Id = airline_id).all()
        return flights
    
    def get_arrival_flights(destination_country_id):
        startdate = datetime.datetime.now()
        flights = Flights.objects.filter(Destination_Country_Id = destination_country_id, Landing_Time__range = (startdate, startdate+datetime.timedelta(hours=12))).all()
        return flights
    
    def get_departure_flights(origin_country_id):
        startdate = datetime.datetime.now()
        flights = Flights.objects.filter(Origin_Country_Id = origin_country_id, Departure_Time__range = (startdate, startdate+datetime.timedelta(hours=12))).all()
        return flights

    def get_flights_by_country(country_id):
        
        flights1 = Flights.objects.filter(Destination_Country_Id = country_id).all()
        flights2 = Flights.objects.filter(Origin_Country_Id = country_id).all()
        flights = flights1 | flights2
        return flights

class Customers(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Phone_No = models.CharField(max_length=30, unique=True)
    Credot_Card_No = models.CharField(max_length=30, unique=True)
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.First_Name + self.Last_Name

    def get_customer_by_username(Username):
        Customer = Customers.objects.filter(User_Id__Username=Username).first()
        return Customer

class Tickets(models.Model):
    Flight_Id = models.OneToOneField(Flights, on_delete=models.CASCADE, null=True, unique=True)
    Customer_Id = models.OneToOneField(Customers, on_delete=models.CASCADE, null=True, unique=True)

    def get_tickets_by_customer(customer_id):
        tickets = Tickets.objects.filter(Customer_Id = customer_id).all()
        return tickets

class Administrators(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    User_Id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    def __str__(self):
     	   return self.First_Name + " to "+ self.Last_Name