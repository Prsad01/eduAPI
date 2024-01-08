from rest_framework.permissions import BasePermission


class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'instructor':
            return True

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'student':
            return True
        
class NoPermission(BasePermission):
    def has_permission(self, request, view):
        return False