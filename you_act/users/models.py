from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User
# from djoser.urls.base import User


# Create your models here.


class UserProfile(models.Model):
    '''профиль пользователя'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users_avatar/', blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
