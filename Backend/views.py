from django.http import HttpResponse

def Home(req):
    return HttpResponse("<h1>HOME first <a href='/AirlineApp/index'>index</a></h1>")


    