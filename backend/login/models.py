from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email,password, **extra_fields)
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    ced = models.TextField(max_length=12, unique=True)
    tel = models.TextField(max_length=10)
    nombre = models.TextField(max_length=50)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    @property
    def is_staff(self):
        return self.is_superuser
    
    def __str__(self):
        return self.email