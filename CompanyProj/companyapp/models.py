from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Company(models.Model):
	companyName = models.CharField(max_length=100)
        companylocation = models.CharField(max_length=100)
        TotalEmployees = models.IntegerField()
 
        def __unicode__(self):
        	return self.companyName


class EmployeeDetails(models.Model):
	EmployeeName = models.CharField(max_length=100)
	EmployeeRole = models.CharField(max_length=100)
        Age = models.IntegerField()
        EmpCompany = models.ForeignKey(Company)

        def __unicode__(self):
        	return '%s %s' % (self.EmployeeName, self.EmployeeRole)

class JobOpenings(models.Model):
	EmployeeRole = models.CharField(max_length=100)
	associated_company = models.ForeignKey(Company)

	def __unicode__(self):
        	return '%s' % (self.role_name)

