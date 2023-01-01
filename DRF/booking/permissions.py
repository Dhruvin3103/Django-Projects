from rest_framework import permissions


class userpermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("booking.view_booking"):  # app_name.verb_model_name
                return False
            return False
        return False
