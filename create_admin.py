import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
u, created = User.objects.get_or_create(username='admin', defaults={'email': 'admin@test.com'})
u.set_password('admin123')
u.is_superuser = True
u.is_staff = True
u.save()
print(f'Admin {"creado" if created else "actualizado"}: admin / admin123')
