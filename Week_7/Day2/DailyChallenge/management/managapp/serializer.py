from rest_framework import serializers
from .models import Department, Employee, Task, Project

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'description')
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='employee-detail') #///
    
    department = serializers.HyperlinkedRelatedField(view_name='department-detail', queryset=Department.objects.all())
    
    class Meta:
        model = Employee
        fields = ('name', 'email', 'phone_number', 'department', 'project')
                
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.HyperlinkedRelatedField(view_name='project-detail', queryset=Project.objects.all())
    class Meta:
        model = Task
        fields = ('name', 'description', 'due_date', 'completed', 'project')
        
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date')


# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = ('name', 'description')
        
# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ('name', 'email', 'phone_number', 'department', 'project')
        
        
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('name', 'description', 'due_date', 'completed', 'project')
        
# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ('name', 'description', 'start_date', 'end_date')
