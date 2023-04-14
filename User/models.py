from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
class CustomUser(AbstractUser):
    celular = models.CharField(max_length=50)
    ubicacion = models.IntegerField()
    usuario_nombre = models.CharField(max_length=50)
    usuario_apellido = models.CharField(max_length=50)

        # campos personalizados
    
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set'  # agregamos un related_name personalizado
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set'  # agregamos un related_name personalizado
    )

    

    def __str__(self):
        return self.username