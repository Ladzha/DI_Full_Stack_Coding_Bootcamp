from rest_framework import serializers
from .models import Department, Employee, Task, Project

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='department-detail')
    # department = serializers.HyperlinkedRelatedField(view_name='department-detail', queryset=Department.objects.all())

    class Meta:
        model = Department
        fields = ('name', 'description', 'url')
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')
    # employee = serializers.HyperlinkedRelatedField(view_name='employee-detail', queryset=Employee.objects.all())
    class Meta:
        model = Employee
        fields = ('name', 'email', 'phone_number', 'department', 'project', 'url')
                
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')   
    # task = serializers.HyperlinkedRelatedField(view_name='task-detail', queryset=Task.objects.all())

    class Meta:
        model = Task
        fields = ('name', 'description', 'due_date', 'completed', 'project', 'url')
        
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project-detail')
    # project = serializers.HyperlinkedRelatedField(view_name='project-detail', queryset=Project.objects.all())
    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date', 'url')
