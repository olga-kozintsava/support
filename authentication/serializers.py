from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from authentication.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])

        return user

#
# class RegistrationSerializer(serializers.ModelSerializer):
#     """ Сериализация регистрации пользователя и создания нового. """
#
#     # Убедитесь, что пароль содержит не менее 8 символов, не более 128,
#     # и так же что он не может быть прочитан клиентской стороной
#     password = serializers.CharField(
#         max_length=128,
#         min_length=8,
#         write_only=True
#     )
#
#     # Клиентская сторона не должна иметь возможность отправлять токен вместе с
#     # запросом на регистрацию. Сделаем его доступным только на чтение.
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     class Meta:
#         model = User
#         # Перечислить все поля, которые могут быть включены в запрос
#         # или ответ, включая поля, явно указанные выше.
#         fields = ['email', 'username', 'password', 'token']
#
#     def create(self, validated_data):
#         # Использовать метод create_user, который мы
#         # написали ранее, для создания нового пользователя.
#         return User.objects.create_user(**validated_data)
