from rest_framework.permissions import BasePermission

ADMIN_METHODS = ['GET', 'DELETE', 'PUT', 'PATCH']


class IsAdminOrPostOnly(BasePermission):
    message = 'This method is not allowed'

    def has_permission(self, request, view):
        if request.method in ADMIN_METHODS and request.user and not request.user.is_staff:
            return False
        return True

#
# class IsAdmin(BasePermission):
#
#     def has_permission(self, request, view):
#         return request.user and request.user.is_superuser


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        else:
            return obj.author == request.user
