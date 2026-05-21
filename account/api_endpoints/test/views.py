from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import (
    RegisterSerializer,
    RegisterVerifySerializer,
    PasswordResetRequestSerializer,
    PasswordResetVerifySerializer,
    PasswordResetConfirmSerializer,
)
from account.email import send_email_code, verify_email_code

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Ro'yxatdan o'tish — kod yuborish",
        operation_description=(
            "Foydalanuvchi ma'lumotlarini qabul qiladi va emailga 4 xonali tasdiqlash kodi yuboradi.\n\n"
            "Keyingi qadam: `/auth/register/verify/` ga kodni yuboring."
        ),
        tags=["Ro'yxatdan o'tish"],
        request_body=RegisterSerializer,
        responses={
            200: openapi.Response(
                description="Kod emailga yuborildi",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            example="user@gmail.com manziliga tasdiqlash kodi yuborildi."
                        )
                    }
                )
            ),
            400: openapi.Response(description="Validatsiya xatosi (email band yoki parol xato)"),
            503: openapi.Response(description="Email xizmati ishlamayapti"),
        }
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = data["email"]

        cache.set(f"register_data_{email}", {
            "first_name": data["first_name"],
            "last_name":  data["last_name"],
            "email":      email,
            "phone":      data["phone"],
            "password":   data["password"],
            "role":       data.get("role", "student"),
        }, timeout=60 * 5)

        ok = send_email_code(email)
        if not ok:
            return Response(
                {"detail": "Email yuborishda xatolik yuz berdi. Keyinroq urinib ko'ring."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        return Response(
            {"detail": f"{email} manziliga tasdiqlash kodi yuborildi."},
            status=status.HTTP_200_OK,
        )


class RegisterVerifyView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Ro'yxatdan o'tish — kodni tasdiqlash",
        operation_description=(
            "Emailga yuborilgan 4 xonali kodni tekshiradi va foydalanuvchi accountini yaratadi."
        ),
        tags=["Ro'yxatdan o'tish"],
        request_body=RegisterVerifySerializer,
        responses={
            201: openapi.Response(
                description="Account yaratildi",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            example="Ro'yxatdan o'tish muvaffaqiyatli yakunlandi."
                        )
                    }
                )
            ),
            400: openapi.Response(description="Kod noto'g'ri, muddati o'tgan yoki ma'lumotlar topilmadi"),
        }
    )
    def post(self, request):
        serializer = RegisterVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        code  = serializer.validated_data["code"]

        if not verify_email_code(email, code):
            return Response(
                {"detail": "Kod noto'g'ri yoki muddati o'tgan."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user_data = cache.get(f"register_data_{email}")
        if not user_data:
            return Response(
                {"detail": "Ma'lumotlar topilmadi. Iltimos, qaytadan ro'yxatdan o'ting."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create_user(
            email=user_data["email"],
            password=user_data["password"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            phone=user_data["phone"],
            role=user_data["role"],
            is_confirmed=True,
        )
        cache.delete(f"register_data_{email}")

        return Response(
            {"detail": "Ro'yxatdan o'tish muvaffaqiyatli yakunlandi."},
            status=status.HTTP_201_CREATED,
        )



class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Parol tiklash — kod yuborish",
        operation_description=(
            "Foydalanuvchi emailiga 4 xonali parol tiklash kodi yuboradi.\n\n"
            "Keyingi qadam: `/auth/password/reset/confirm/` ga kodni va yangi parolni yuboring."
        ),
        tags=["Parol tiklash"],
        request_body=PasswordResetRequestSerializer,
        responses={
            200: openapi.Response(
                description="Kod yuborildi",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            example="user@gmail.com manziliga parol tiklash kodi yuborildi."
                        )
                    }
                )
            ),
            400: openapi.Response(description="Email topilmadi"),
            503: openapi.Response(description="Email xizmati ishlamayapti"),
        }
    )
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]

        ok = send_email_code(email)
        if not ok:
            return Response(
                {"detail": "Email yuborishda xatolik yuz berdi."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        return Response(
            {"detail": f"{email} manziliga parol tiklash kodi yuborildi."},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Parol tiklash — kodni tasdiqlash va yangi parol",
        operation_description=(
            "Emailga yuborilgan kodni tekshirib, yangi parolni saqlaydi."
        ),
        tags=["Parol tiklash"],
        request_body=PasswordResetConfirmSerializer,
        responses={
            200: openapi.Response(
                description="Parol yangilandi",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "detail": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            example="Parol muvaffaqiyatli yangilandi."
                        )
                    }
                )
            ),
            400: openapi.Response(description="Kod noto'g'ri yoki parollar mos kelmadi"),
            404: openapi.Response(description="Foydalanuvchi topilmadi"),
        }
    )
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email        = serializer.validated_data["email"]
        code         = serializer.validated_data["code"]
        new_password = serializer.validated_data["new_password"]

        if not verify_email_code(email, code):
            return Response(
                {"detail": "Kod noto'g'ri yoki muddati o'tgan."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(email=email, is_active=True).first()
        if not user:
            return Response(
                {"detail": "Foydalanuvchi topilmadi."},
                status=status.HTTP_404_NOT_FOUND,
            )

        user.set_password(new_password)
        user.save(update_fields=["password"])

        return Response(
            {"detail": "Parol muvaffaqiyatli yangilandi."},
            status=status.HTTP_200_OK,
        )