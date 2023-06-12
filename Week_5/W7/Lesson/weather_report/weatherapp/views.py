from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Report, Forecaster
from .serializer import ReportSerializer, ForecasterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveDestroyAPIView
from rest_framework import permissions
from django.contrib.auth.models import User
from .promissions import IsForecaster 


# @csrf_exempt
# def post_view(request):
#     #GET
#     queryset = Report.objects.all()
#     serializer = PostSerializer(queryset, many = True)
#     return JsonResponse(data=serializer.data, safe=False)



class ReportView(APIView):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs: 
            report = Report.objects.get(id=kwargs['pk'])
            serializer = ReportSerializer(report)
            return Response(serializer.data)
        else:
            queryset = Report.objects.all()
            serializer = ReportSerializer(queryset, many = True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ReportSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        report = Report.objects.get(id=pk)
        report.delete()
        return Response(status=HTTP_204_NO_CONTENT)
     
    def put(self, request, pk, *args, **kwargs):
        report = Report.objects.get(id=pk)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ReportListView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView): #vsegda d sochetanii s chem-to
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
    def get(self, request, *args, **kwargs):   # all objects
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class ReportListView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView): #vsegda d sochetanii s chem-to
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer
    
#     def get(self, request, *args, **kwargs):   # all objects
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
class ReportMixinView(generics.ListCreateAPIView): #s nim ne nuzhni mixin v skobkah
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
    def get(self, request, *args, **kwargs):   # all objects
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
   
   
class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
        
class ReportDetailView(generics.RetrieveAPIView): 
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    
class ReportDeletelView(generics.DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
    
class ReportRetriveDeletelView(generics.RetrieveDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (permissions.AllowAny, IsForecaster)



class ForecasterDetailView(generics.RetrieveAPIView):
    queryset = Forecaster.objects.all()
    serializer_class = ForecasterSerializer
    permission_classes = (permissions.IsAuthenticated, )

#APIView long and customize detail structure for complex situations for several serializer 
#generics.GenericAPIView + Mixin hybrid of generic API and additional functionalities
#generic.APIViews (generics.RetrieveAPIView) doing the CRUD-create, retrive, update, delete

#APIView - For more complex situations (using multiple serializers or customized Response)
#generics.GenericAPIView + Mixins (mixins.ListModelMixin) - hybrid of generic API and additional functionalities
#generic APIView (generics.RetrieveAPIView) - doing the most common actions (CRUD - create retrieve update delete)

# ListAPIView get 
# RetrieveAPIView get with pk 1
# ListCreateAPIView post and get