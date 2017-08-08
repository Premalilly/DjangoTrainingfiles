from rest_framework import serializers
from .models import Company, EmployeeDetails, JobOpenings

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'

class JobOpeningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpenings
        fields = '__all__'
