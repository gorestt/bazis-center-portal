
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile

class Command(BaseCommand):
    help = 'Создаёт демо-пользователей admin / manager / client'

    def handle(self, *args, **options):
        data = [
            ('admin', 'admin123', 'admin'),
            ('manager', 'manager123', 'manager'),
            ('client', 'client123', 'client'),
        ]
        for username, password, role in data:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.is_staff = True if role in ('admin','manager') else False
                user.is_superuser = True if role == 'admin' else False
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Создан пользователь {username}/{password}'))
            profile, _ = Profile.objects.get_or_create(user=user, defaults={'role': role})
            profile.role = role
            profile.save()
        self.stdout.write(self.style.SUCCESS('Демо-пользователи успешно созданы'))
