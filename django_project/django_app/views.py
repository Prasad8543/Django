from django.shortcuts import render
from rest_framework import generics
from django_app.models import Department, Employee
from rest_framework.response import Response
from django_app.serializers import DepartmentListCreateSerializer, EmployeeListCreateSerializer

# Create your views here.

class EmployeeListCreate(generics.ListCreateAPIView):
    serializer_class=EmployeeListCreateSerializer

    def get_queryset(self):
        return Employee.objects.all()

class DepartmentListCreate(generics.ListCreateAPIView):
    serializer_class=DepartmentListCreateSerializer

    def get_queryset(self):
        return Department.objects.all()


