from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
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

class AppUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class AppUser(AbstractBaseUser):
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='이메일')
    username = models.CharField(max_length=50, unique=True, verbose_name='유저네임')
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name='비밀번호')
    profile_image = models.ImageField(upload_to='media/profile/', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    last_login = models.DateTimeField(auto_now=True, verbose_name='마지막 로그인')

    objects = AppUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'user'
        verbose_name = "사용자"
        verbose_name_plural = "사용자"