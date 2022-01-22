from rest_framework import serializers
from firstapp.models import Deparments,Employees

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deparments
        fields = ('DepartmentId',
                  'DepartmentName')
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining')