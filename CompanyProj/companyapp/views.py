from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from .models import Company, EmployeeDetails, JobOpenings
from .serializers import CompanySerializer, EmployeeDetailsSerializer, JobOpeningsSerializer
from drf_multiple_model.views import MultipleModelAPIView


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeDetailsViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('EmployeeRole',)

class JobOpeningsViewViewSet(viewsets.ModelViewSet):
    queryset = JobOpenings.objects.all()
    serializer_class = JobOpeningsSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('role_name',)


class SearchFilterView(MultipleModelAPIView):
    queryList = ((EmployeeDetails.objects.all(), EmployeeDetailsSerializer),
                 (JobOpenings.objects.all(), JobOpeningsSerializer))
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('EmployeeRole',)




