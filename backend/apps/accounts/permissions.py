from rest_framework.permissions import BasePermission


class IsAdministrator(BasePermission):
    """
    Allows access to authenticated staff members
    or users with the ADMIN role.
    """

    message = "Only administrators can perform this action."

    def has_permission(self, request, view):
        user = request.user

        return (
            user
            and user.is_authenticated
            and (user.is_staff or getattr(user, "role", None) == "ADMIN")
        )
