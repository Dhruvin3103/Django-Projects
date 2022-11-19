from rest_framework import permissions


class isstaffpermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if request.user.is_staff:
            if user.has_perm({'basicapi.add_movie'}):#app_name.verb_model_name
                return True
            if user.has_perm({'basicapi.view_movie'}):#app_name.verb_model_name
                return True

            return False

        return False
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user