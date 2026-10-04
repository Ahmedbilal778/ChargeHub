from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        USER = "USER", "User"
        ADMIN = "ADMIN", "Admin"

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )

    def __str__(self):
        return self.username