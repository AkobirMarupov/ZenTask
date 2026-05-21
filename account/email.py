from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings
import random


def generate_email_code() -> str:
    """4 xonali tasdiqlash kodi"""
    return str(random.randint(1000, 9999))


def send_email_code(email: str) -> bool:
    code = generate_email_code()
    try:
        send_mail(
            subject="Tasdiqlash kodi",
            message=f"Tasdiqlash kodingiz: {code}\n\nKod 5 daqiqa davomida amal qiladi.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        # Kodni cache ga saqlash
        cache.set(f"email_code_{email}", code, timeout=60 * 5)
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] {email}: {e}")
        return False


def verify_email_code(email: str, code: str) -> bool:
    cached_code = cache.get(f"email_code_{email}")
    if cached_code and cached_code == str(code):
        cache.delete(f"email_code_{email}")
        return True
    return False