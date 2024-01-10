from rest_framework.permissions import BasePermission


class InstrucatorOrStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (
                request.user.groups.filter(name='students_group').exists() or 
                request.user.groups.filter(name='instructors_group').exists()
            )

class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == 'instructor':
                return True

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == 'student':
                return True
        
class NoPermission(BasePermission):
    def has_permission(self, request, view):
        return False