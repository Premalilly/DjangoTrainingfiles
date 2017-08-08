# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-03 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100)),
                ('companylocation', models.CharField(max_length=100)),
                ('TotalEmployees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeName', models.CharField(max_length=100)),
                ('EmployeeRole', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('EmpCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='JobOpenings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('associated_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyapp.Company')),
            ],
        ),
    ]