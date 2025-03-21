from rest_framework.permissions import BasePermission
from datetime import date, timedelta
from django.utils.timezone import now


class CanDeletePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            obj = view.get_object()
            if date.today().weekday() > 4:
                return False
            if now() - obj.created_at > timedelta(minutes=2):
                return False
        return True

class CreatePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            if date.today().weekday() > 4:
                return False
            return True
        return True