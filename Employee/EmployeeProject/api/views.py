from django.shortcuts import render
from rest_framework import viewsets

from api.models import Employee
from api.serializers import EmployeeSerializer



class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer