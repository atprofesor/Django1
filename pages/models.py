from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200) # Un título corto
    content = models.TextField()               # Un texto largo

    def __str__(self):
        return self.title # Esto hace que en el admin se vea el título y no "Post object"