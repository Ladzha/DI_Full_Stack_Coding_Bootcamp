from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND



class StudentListView(APIView):
    
    def get(self, request, *args, **kwargs):
        date_joined = request.GET.get('date_joined')
        if date_joined:
            queryset = Student.objects.filter(date_joined=date_joined)
        else:
            queryset = Student.objects.all()

        serializer = StudentSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        pass

class StudentDetailView(APIView): 
    def get(self, request, pk, *args, **kwargs):
        try:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except:
            return Response(status=HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)
     
    def put(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
                
