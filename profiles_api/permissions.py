import imp
from pickle import PERSID
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ALlow User to update their  own profile"""

    def has_object_permission(self,request, view, obj):
        """Checkuser is having to edit theri own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

