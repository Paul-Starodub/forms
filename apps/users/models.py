from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.users.utils import profile_image_file_path
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    profile_image = models.ImageField(
        blank=True,
        upload_to=profile_image_file_path,
        verbose_name=_("Profile image"),
    )

    def __str__(self) -> str:
        return self.username
