# backends.py
from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import PermissionDenied
from .models import HouseHelp, Employer


class HouseHelpBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = HouseHelp.objects.get(username=username)
            if user.check_password(password):
                if not user.is_active:
                    raise PermissionDenied("This account is inactive.")
                return user
        except HouseHelp.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return HouseHelp.objects.get(pk=user_id)
        except HouseHelp.DoesNotExist:
            return None


class EmployerBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Employer.objects.get(username=username)
            if user.check_password(password):
                if not user.is_active:
                    raise PermissionDenied("This account is inactive.")
                return user
        except Employer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employer.objects.get(pk=user_id)
        except Employer.DoesNotExist:
            return None
