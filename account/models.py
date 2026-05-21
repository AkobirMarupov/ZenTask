from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from common.models import BaseModel
from account.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):

    class Role(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        STUDENT = 'student', _('Student')
        TEACHER = 'teacher', _('Teacher')
    
    email      = models.EmailField(unique=True)
    password   = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50, blank=True)
    last_name  = models.CharField(max_length=50, blank=True)
    phone      = models.CharField(max_length=20)          # 8 → 20 qildim, +998901234567 sig'sin
    date_joined = models.DateTimeField(auto_now_add=True)
    role        = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT, verbose_name=_("Rol"))
    is_confirmed = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"