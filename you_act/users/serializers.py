from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = User(
        email=self.validated_data['email'], # Назначаем Email
        username=self.validated_data['username'], # Назначаем Логин
        )
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        # создаем и сохраняем профиль пользователя
        profile = UserProfile(user=user)
        profile.save()
        # Возвращаем нового пользователя 
        return user



class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
