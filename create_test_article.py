import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from blog.models import Article

User = get_user_model()

# Buscar o crear el editor1 para ser autor
user, created = User.objects.get_or_create(
    username='editor1',
    defaults={'email': 'editor@test.com'}
)
if created:
    user.set_password('editando4321')
    user.save()
    print('Usuario editor1 creado')

# Crear articulo de prueba si no existe
article, created = Article.objects.get_or_create(
    title='Articulo de Prueba',
    defaults={
        'content': 'Este es un articulo de prueba para probar permisos.',
        'author': user,
        'published': False
    }
)

if created:
    print(f'✅ Articulo creado con ID: {article.pk}')
else:
    print(f'✅ Articulo ya existe con ID: {article.pk}')

print(f'\nPrueba ahora:')
print(f'- Lista: http://localhost:8080/blog/articles/')
print(f'- Eliminar: http://localhost:8080/blog/articles/{article.pk}/delete/')
print(f'- Publicar: http://localhost:8080/blog/articles/{article.pk}/publish/')
