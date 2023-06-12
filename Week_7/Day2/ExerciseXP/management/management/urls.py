"""
URL configuration for management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from managapp.views import DepartmentListView, EmployeeListView, TaskListView, ProjectListView
from managapp.views import DepartmentListAPIView, DepartmentCreateAPIView, EmployeeListAPIView, EmployeeCreateAPIView, ProjectListAPIView, ProjectRetrieveAPIView, ProjectUpdateAPIView, ProjectDestroyAPIView, TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, TaskDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')),
    
    path('api/departments/', DepartmentListAPIView.as_view(), name='departments-list'),
    path('api/departments/create/', DepartmentCreateAPIView.as_view(), name='departments-list-create'),
    
    path('api/employees/', EmployeeListAPIView.as_view(), name='employees-list'),
    path('api/employees/create/', EmployeeCreateAPIView.as_view(), name='employees-list-create'),
    
    path('api/tasks/', TaskListAPIView.as_view(), name='tasks-list'),
    path('api/taskdetail/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-detail'),
    path('api/taskupdate/<int:pk>/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('api/taskdelete/<int:pk>/', TaskDestroyAPIView.as_view(), name='task-detail'),

    
    path('api/projects/', ProjectListAPIView.as_view(), name='projects-list'),
    path('api/projectdetail/<int:pk>/', ProjectRetrieveAPIView.as_view(), name='project-detail'),
    path('api/projectupdate/<int:pk>/', ProjectUpdateAPIView.as_view(), name='project-update'),
    path('api/projectdelete/<int:pk>/', ProjectDestroyAPIView.as_view(), name='project-detail'),
]


