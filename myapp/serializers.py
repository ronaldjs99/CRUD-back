from rest_framework import serializers
from .models import Company, Profile
#Serializers in DRF allow complex data types, such as Django models, 
# to be converted to JSON, XML, or other content types for use in the API.

#serializer for Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

#serializer for Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'