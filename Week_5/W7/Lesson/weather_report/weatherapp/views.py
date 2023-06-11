from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Report
from .serializer import ReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


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
                