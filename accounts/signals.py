from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_migrate)
def create_demo_users(sender, **kwargs):
    if sender.name != 'accounts':
        return
    users_data = [
        ('admin', 'admin123', 'admin', True, True),
        ('manager', 'manager123', 'manager', True, False),
        ('client', 'client123', 'client', False, False),
    ]
    for username, password, role, is_staff, is_superuser in users_data:
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.password = make_password(password)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.role = role
        profile.save()
