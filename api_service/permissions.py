
from rest_framework import permissions

class IsCartOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to see and edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            # print('--------------------------')
            if request.user.customer == obj.customer_id:
                return True
            return False
            

        # Write permissions are only allowed to the owner of the snippet.
        if request.user.customer == obj.customer_id and obj.status == 'u':
            return True
        return False


class IsOrderOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to see and edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            # print('--------------------------')
            if request.user.customer == obj.cart_id.customer_id:
                return True
            return False
            

        # Write permissions are only allowed to the owner of the snippet.
        if request.user.customer == obj.cart_id.customer_id and obj.cart_id.status == 'u':
            return True
        return False