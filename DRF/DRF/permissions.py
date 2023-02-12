from rest_framework import permissions


class moviepermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_superuser:
            if not user.has_perm('movie.view_movie') and request.method=='GET':
                return True
            return False
        return False
        if user.is_theatre_operator and not user.is_superuser:
            return True
        if user.is_movie_operator and not user.is_superuser:
            return True

class bookingpermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_superuser:
            return True
        if user.is_movie_operator and not user.is_superuser:
            return True
        if user.is_theatre_operator and not user.is_superuser:
            return True

class theatrepermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_superuser:
            if not user.has_perm('theatre.view_theatre') and request.method=='GET':
                return True
            return False
        return False
        if user.is_theatre_operator and not user.is_superuser:
            return True
        if user.is_movie_operator and not user.is_superuser:
            if not user.has_perm('theatre.view_theatre') and request.method=='GET':
                return True
            return False
        return False

