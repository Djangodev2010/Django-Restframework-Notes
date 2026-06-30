from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of the snippet to edit them
    and all read only permissions to all unauthorized users
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for all users, so we will
        # allow all safe method GET, HEAD, OPTION
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check is the requested user is the owner of the snippet, if yes,
        # then authorize them for the write permissions
        return request.user == obj.owner
