from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'student':
           if request.method in ['GET','POST']:
            return True
        
class NoPermission(BasePermission):
    def has_permission(self, request, view):
        return False