from django.db import models
from users.models.user_models import AppUser
from utils.enums import SocialAccountEnum


class SocialAccount(models.Model):
    class Meta:
        verbose_name = "소셜계정"
        verbose_name_plural = "소셜계정"

    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    provider = models.CharField(
        max_length=10, default=None, null=True, choices=SocialAccountEnum.choices()
    )
    uid = models.CharField(
        max_length=255, default="", null=False, blank=False, unique=True
    )

    def __str__(self):
        return self.user.username
