from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('domestic', domestic, name="domestic"),
    path('about/', about, name="about"),
    
    path('booking/', booking, name="booking"),
    path('contact/', contact, name="contact"),
    path('service/', service, name="service"),
    path('packages/', packages, name="packages"),
    path('destinations/', destinations, name="destinations"),

    
    
    






]