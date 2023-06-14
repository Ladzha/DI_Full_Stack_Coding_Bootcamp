from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from .models import DepartmentAdmin

# class IsDepartmentAdmin(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         #SAFE_METHOD: GET< HEAD< OPTIONS
#         if request.user.IsAdminUser:
#             return True
#         else:
#             return False
        
class IsDepartmentAdmin(permissions.BasePermission):  
    pass
    # def has_permission(self, request, view):
    #     if request.user.IsAdminUser:
    #         return True
    #     else:
    #         return False
