from rest_framework import serializers
from .models import Report, Forecaster
from django.contrib.auth.models import User

class ReportSerializer(serializers.ModelSerializer):
    
    forecaster = serializers.HyperlinkedRelatedField(view_name='forecaster-detail', queryset=Forecaster.objects.all())
    
    class Meta:
        model = Report
        fields = ('location', 'temperature', 'created_at', 'forecaster')
        
        
class ForecasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecaster
        fields = ('id',)