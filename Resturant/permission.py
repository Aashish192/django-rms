from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsWorkerOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True


        return (
            request.user
            and request.user.is_authenticated
            and request.user.role in ['worker', 'admin']
        )


class IsWorkerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
                request.user
                and request.user.is_authenticated
                and request.user.role in ['worker', 'admin']
            )
        
class IsWorkerOrIsAdminOrPostOnly(BasePermission):
    """
    Allows access only for POST requests.
    Blocks all other request methods like GET, PUT, DELETE, etc.
    """
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and user.role in ['admin', 'worker']:
            return True
        return request.method == 'POST'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated and user.role == 'admin':
            return True
        return False