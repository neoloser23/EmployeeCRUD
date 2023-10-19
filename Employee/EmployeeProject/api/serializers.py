from rest_framework import serializers
from api.models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"