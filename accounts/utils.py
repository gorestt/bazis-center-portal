from functools import wraps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render

def get_role(user):
    if not user.is_authenticated:
        return 'anon'
    profile = getattr(user, 'profile', None)
    if profile:
        return profile.role
    if user.is_superuser:
        return 'admin'
    if user.is_staff:
        return 'manager'
    return 'client'

def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped(request, *args, **kwargs):
            role = get_role(request.user)
            if role not in roles:
                return HttpResponseForbidden(render(request, '403.html'))
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
