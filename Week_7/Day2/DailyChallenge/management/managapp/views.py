from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Department, Employee, Task, Project
from .serializer import DepartmentSerializer, EmployeeSerializer, TaskSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsDepartmentAdmin

from rest_framework import generics

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveDestroyAPIView


#*********departments*********#
class DepartmentListAPIView(generics.ListAPIView): 
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes= (IsDepartmentAdmin, )
    
class DepartmentRetrieveAPIView(generics.RetrieveAPIView): 
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer 
    permission_classes= (IsDepartmentAdmin, )  


#*********employees*********#

class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

        
class EmployeeCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes= (IsDepartmentAdmin, )
    
class EmployeeRetrieveAPIView(generics.RetrieveAPIView): 
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes= (IsDepartmentAdmin, )      
        
#*********projects*********#  

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    
class ProjectRetrieveAPIView(generics.RetrieveAPIView): 
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes= (IsDepartmentAdmin, )
        
class ProjectUpdateAPIView(generics.UpdateAPIView):
    queryset =Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes= (IsDepartmentAdmin, )   
    
class ProjectDestroyAPIView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes= (IsDepartmentAdmin, )
    
#*********tasks*********#

class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskRetrieveAPIView(generics.RetrieveAPIView): 
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes= (IsDepartmentAdmin, )
        
class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset =Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes= (IsDepartmentAdmin, )   

class TaskDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes= (IsDepartmentAdmin, )

