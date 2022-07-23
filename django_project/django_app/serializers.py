from django_app.models import Employee,Department
from rest_framework import serializers

class EmployeeListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=Employee
        fields=["id","first_name","last_name","date_of_birth","salary","department"]

class DepartmentListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=Department
        fields=["id","name"]