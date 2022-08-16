
from django.urls import include, path
from .views import views, users_view, token_view, Airline_Companies_view,login_view, countries_view, flights_view, customers_view, administrators_view, tickets_view
from .views.token_view import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework import routers
from .views.users_view import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Users urls:
    # path('users', users_view.users),
    # path('users/<pk>', users_view.users),
    path('Airline_Companies/', Airline_Companies_view.airline_Companies),
    path('Airline_Companies/<pk>', Airline_Companies_view.airline_Companies),
    path('countries/', countries_view.countries),
    path('countries/<pk>', countries_view.countries),
    path('flights/', flights_view.flight),
    path('flights/<pk>', flights_view.flight),
    path('flightsByCountry/<pk>', flights_view.flightByCountry),
    path('customers/', customers_view.customers),
    path('customers/<pk>', customers_view.customers),
    path('tickets/', tickets_view.tickets),
    path('tickets/<pk>', tickets_view.tickets),
    path('administrator/', administrators_view.administrator),
    path('administrator/<pk>', administrators_view.administrator),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', login_view.login)
]
