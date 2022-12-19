from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

        # def create(self, validated_data):
        #     password = validated_data.pop('password')
        #     password2 = validated_data.pop('password2')
        #     if self.validated_data['password'] != self.validated_data['password2']:
        #         print('-'*50, 'пароли не совпадают')
        #         raise serializers.ValidationError({password: "Пароли не совпадает"})
        #     print('-'*50, 'пароли совпадают')
        #     validated_data.pop('password2')
        #     user = User(**validated_data)
        #     user.set_password(password)
        #     user.save()
        #     return user
        
    # def save(self, *args, **kwargs):
    #     # Создаём объект класса User
    #     user = User(
    #     email=self.validated_data['email'], # Назначаем Email
    #     username=self.validated_data['username'], # Назначаем Логин
    #     )
    #     # Проверяем на валидность пароль
    #     password = self.validated_data['password']
    #     # Проверяем на валидность повторный пароль
    #     password2 = self.validated_data['password2']
    #     # Проверяем совпадают ли пароли
    #     if password != password2:
    #     # Если нет, то выводим ошибку
    #         raise serializers.ValidationError({password: "Парольи не совпадает"})
    #     # Сохраняем пароль
    #     user.set_password(password)
    #     # Сохраняем пользователя
    #     user.save()
    #     # Возвращаем нового пользователя 
    #     return user
                


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    real_name = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'
