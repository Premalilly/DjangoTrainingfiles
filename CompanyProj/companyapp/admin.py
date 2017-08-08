from django.contrib import admin
from .models import Company, EmployeeDetails, JobOpenings
# Register your models here.


admin.site.register(Company)
admin.site.register(EmployeeDetails)
admin.site.register(JobOpenings)
