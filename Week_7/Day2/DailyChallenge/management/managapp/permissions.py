from rest_framework import permissions
# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.permissions import BasePermission
from .models import DepartmentAdmin

class IsDepartmentAdmin(permissions.BasePermission):  
    def has_object_permission(self, request, view, admin):
        return hasattr(request.user, 'DepartmentAdmin')
    # def has_object_permission(self, request, view, obj):
    #    return request.user and request.user.DepartmentAdmin
