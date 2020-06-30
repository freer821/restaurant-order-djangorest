from rest_framework import permissions


class IsAdminRole(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        # Instance must have an attribute named `owner`.
        return request.user.profile.role == 'admin'