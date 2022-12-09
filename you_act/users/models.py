from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class UserManager(auth_models.BaseUserManager):

#     def create_user(self, first_name: str, last_name: str, email: str, password: str = None, is_staff=False, is_superuser=False) -> "User":
#         if not email:
#             raise ValueError('Введите адрес електронной почты!')
#         if not first_name:
#             raise ValueError('У пользователя должно быть имя!')
#         if not last_name:
#             raise ValueError('У пользователя должна быть фамилия')

#         user = self.model(email=self.normalize_email(email))
#         user.first_name = first_name
#         user.last_name = last_name
#         user.set_password(password)
#         user.is_active = True
#         user.is_staff = is_staff
#         user.is_superuser = is_superuser
#         user.save()

#         return user


#     def create_superuser(self, first_name: str, last_name: str, email: str, password: str) -> "User":
#         user = self.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             password=password,
#             is_staff=True,
#             is_superuser=True
#         )

#         user.save()

#         return user


# class User(AbstractUser):
    # first_name = models.CharField(verbose_name='Имя', max_length=255)
    # last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    # email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    # password = models.CharField(max_length=255)
    # username = None
    # pass
