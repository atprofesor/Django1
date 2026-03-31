from django.contrib import admin

# Register your models here.

from .models import Post # Importamos el modelo

admin.site.register(Post)