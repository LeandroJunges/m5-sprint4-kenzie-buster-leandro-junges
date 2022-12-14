from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False


class IsUserOrAdm(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj:User):
        return request.user.is_authenticated and (request.user.is_employee or obj == request.user)