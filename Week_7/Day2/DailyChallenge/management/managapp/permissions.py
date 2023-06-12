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
    def has_permission(self, request, user):
        return hasattr(request.user)

# class IsForecaster(permissions.IsAuthenticated):
#     def has_object_permission(self, request, view, obj):
#         user = request.user
#         #SAFE_METHOD: GET< HEAD< OPTIONS
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         elif hasattr(user, 'forecaster'):
#             return True
#         else:
#             return False