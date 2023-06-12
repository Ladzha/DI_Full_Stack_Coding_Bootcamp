"""
URL configuration for weather_report project.

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
from weatherapp.views import ReportView, ReportListView, ReportMixinView, ReportDetailView, ForecasterDetailView, ReportDeletelView, ReportRetriveDeletelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')),
    path('api/report/', ReportView.as_view(), name='report'),
    path('api/report/<int:pk>', ReportView.as_view(), name='report-detail'),
    path('api/reportmixinxtlist/', ReportMixinView.as_view(), name='reportlist'),
    
    path('api/reportlist/', ReportListView.as_view(), name='reportlist'),
    path('api/reportdetail/<int:pk>/', ReportDetailView.as_view(), name='reportdetail'),
    path('api/reportdelete/<int:pk>/', ReportDeletelView.as_view(), name='reportdelete'),
    path('api/reportretrivedelete/<int:pk>/', ReportRetriveDeletelView.as_view(), name='reportdelete'),
    path('api/user/<int:pk>/', ForecasterDetailView.as_view(), name='forecaster-detail'),


]
