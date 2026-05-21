from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()



class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=["student", "teacher"], default="student")

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Bu email allaqachon ro'yxatdan o'tgan.")
        return value

    def validate_password(self, value):
        validate_password(value)
        return value



class RegisterVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    code  = serializers.CharField(min_length=4, max_length=4)


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value, is_active=True).exists():
            raise serializers.ValidationError("Bu email bilan foydalanuvchi topilmadi.")
        return value


class PasswordResetVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    code  = serializers.CharField(min_length=4, max_length=4)


class PasswordResetConfirmSerializer(serializers.Serializer):
    email            = serializers.EmailField()
    code             = serializers.CharField(min_length=4, max_length=4)
    new_password     = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "Parollar mos kelmadi."})
        validate_password(attrs["new_password"])
        return attrs