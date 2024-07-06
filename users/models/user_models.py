from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class AdminUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class Admin(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)

    objects = AdminUserManager()

    class Meta:
        db_table = 'admin_user'
        verbose_name = "관리자"
        verbose_name_plural = "관리자"

class AppUser(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    profile_image = models.ImageField(upload_to='media/profile/', null=True, blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = "사용자"
        verbose_name_plural = "사용자"