from rest_framework import permissions

# class IsOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
        
#         #SAFE_METHOD: GET< HEAD< OPTIONS
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         elif hasattr(request.user, 'forecaster'):
#             return True
#         else:
#             return False
        
class IsForecaster(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user
        #SAFE_METHOD: GET< HEAD< OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        elif hasattr(user, 'forecaster'):
            return True
        else:
            return False
        
        
        
        
# permissions.IsAuthenticated - if user is logged in
# permissions.IsAdminUser - if user is staff user
# permissions.AllowAny - everyone can access
# permissions.IsAuthenticatedOrReadOnly - if not logged in then can only read