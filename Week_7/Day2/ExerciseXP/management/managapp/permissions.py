from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        #SAFE_METHOD: GET< HEAD< OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        elif hasattr(request.user, 'forecaster'):
            return True
        else:
            return False