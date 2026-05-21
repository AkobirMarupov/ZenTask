# from django.urls import path
# from account.api_endpoints.auth import LoginAPIView
# from account.api_endpoints.send_email import UserRegisterCreateAPIView, UserRegisterConfirmAPIView



# # urlpatterns = [
# #     path('register/', UserRegisterCreateAPIView.as_view(), name='register-user'),
# #     path('register/confirm/', UserRegisterConfirmAPIView.as_view(), name='user-register-confirm'),

# #     path('login/', LoginAPIView.as_view(), name='login'),
# # ]

# from account.api_endpoints.test.views import (
#     SendSmsCodeView,
#     VerifySmsCodeView,
#     SendEmailVerificationView,
#     VerifyEmailTokenView,
#     PasswordResetRequestView,
#     PasswordResetConfirmView,
#     SmsPasswordResetRequestView,
#     SmsPasswordResetConfirmView,
# )
 
# urlpatterns = [
#     # SMS tasdiqlash
#     path("auth/sms/send/",              SendSmsCodeView.as_view(),             name="sms-send"),
#     path("auth/sms/verify/",            VerifySmsCodeView.as_view(),           name="sms-verify"),
 
#     # Email tasdiqlash
#     path("auth/email/send-verification/", SendEmailVerificationView.as_view(), name="email-verify-send"),
#     path("auth/email/verify/",           VerifyEmailTokenView.as_view(),       name="email-verify"),
 
#     # Parol tiklash — email
#     path("auth/password/reset/",         PasswordResetRequestView.as_view(),   name="password-reset"),
#     path("auth/password/reset/confirm/", PasswordResetConfirmView.as_view(),   name="password-reset-confirm"),
 
#     # Parol tiklash — SMS
#     path("auth/password/sms-reset/",         SmsPasswordResetRequestView.as_view(),  name="sms-password-reset"),
#     path("auth/password/sms-reset/confirm/", SmsPasswordResetConfirmView.as_view(),  name="sms-password-reset-confirm"),
# ]


from django.urls import path
from account.api_endpoints.test.views import (
    RegisterView,
    RegisterVerifyView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)

urlpatterns = [
    # Ro'yxatdan o'tish
    path("auth/register/",        RegisterView.as_view(),       name="register"),
    path("auth/register/verify/", RegisterVerifyView.as_view(), name="register-verify"),

    # Parol tiklash
    path("auth/password/reset/",         PasswordResetRequestView.as_view(), name="password-reset"),
    path("auth/password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
]


# ══════════════════════════════════════════
# settings.py ga qo'shish (Gmail SMTP)
# ══════════════════════════════════════════

# EMAIL_BACKEND       = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST          = "smtp.gmail.com"
# EMAIL_PORT          = 587
# EMAIL_USE_TLS       = True
# EMAIL_HOST_USER     = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # Gmail App Password

# .env ga qo'shish:
# EMAIL_HOST_USER=sizning@gmail.com
# EMAIL_HOST_PASSWORD=xxxx xxxx xxxx xxxx