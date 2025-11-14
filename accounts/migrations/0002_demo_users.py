
from django.db import migrations

def create_demo_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('accounts', 'Profile')

    data = [
        ('admin', 'admin123', 'admin', True, True),
        ('manager', 'manager123', 'manager', True, False),
        ('client', 'client123', 'client', False, False),
    ]
    for username, password, role, is_staff, is_superuser in data:
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password(password)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        profile, _ = Profile.objects.get_or_create(user=user, defaults={'role': role})
        profile.role = role
        profile.save()

def reverse_func(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    for username in ['admin','manager','client']:
        try:
            User.objects.get(username=username).delete()
        except User.DoesNotExist:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_demo_users, reverse_func),
    ]
