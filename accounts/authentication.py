import sys
from accounts.models import ListUser, Token
from django.contrib.auth.backends import BaseBackend


class PasswordlessAuthenticationBackend(object):
    """Authorization processor without password"""
    def authenticate(self, request, uid=None):
        """Authorization"""
        print('uid', uid, file=sys.stderr)
        if not Token.objects.filter(uid=uid).exists():
            print('no token found', file=sys.stderr)
            return None
        token = Token.objects.get(uid=uid)
        print('got token', file=sys.stderr)
        try:
            user = ListUser.objects.get(email=token.email)
            print('got user', file=sys.stderr)
            return user
        except ListUser.DoesNotExist:
            print('new user', file=sys.stderr)
            return ListUser.objects.create(email=token.email)


    def get_user(self, request, email=None):
        """Get User"""

        return ListUser.objects.get(email=email)

