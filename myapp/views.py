from django.shortcuts import render
from .models import Company, Profile
from rest_framework import viewsets
from .serializers import CompanySerializer, ProfileSerializer
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #This attribute specifies the serializer class to be used for converting the Profile model instances into JSON format 
    # for API responses and parsing JSON data for POST requests. 
    # Make sure you have defined the ProfileSerializer class, which should be similar to the one shown in a previous example.
