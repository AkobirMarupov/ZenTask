import random
import requests
from django.conf import settings
from django.core.cache import cache


def generate_sms_code() -> str:
    """4 xonali tasdiqlash kodi yaratish"""
    return str(random.randint(1000, 9999))


def get_eskiz_token() -> str:
    token = cache.get("eskiz_token")
    if token:
        return token

    response = requests.post(
        "https://notify.eskiz.uz/api/auth/login",
        data={
            "email": settings.ESKIZ_EMAIL,
            "password": settings.ESKIZ_PASSWORD,
        },
        timeout=10,
    )
    response.raise_for_status()
    token = response.json()["data"]["token"]
    cache.set("eskiz_token", token, timeout=60 * 29)
    return token


def send_sms_code(phone: str) -> str | None:
    code = generate_sms_code()
    try:
        token = get_eskiz_token()
        response = requests.post(
            "https://notify.eskiz.uz/api/message/sms/send",
            headers={"Authorization": f"Bearer {token}"},
            data={
                "mobile_phone": str(phone),
                "message": f"Tasdiqlash kodingiz: {code}\nKod 5 daqiqa amal qiladi.",
                "from": settings.ESKIZ_SENDER,  # "4546" yoki o'z nomingiz
            },
            timeout=10,
        )
        response.raise_for_status()

        cache.set(f"sms_code_{phone}", code, timeout=60 * 5)
        return code

    except requests.RequestException as e:
        print(f"[SMS ERROR] {phone}: {e}")
        return None


def verify_sms_code(phone: str, code: str) -> bool:
    """Cache dagi kod bilan taqqoslash va o'chirish"""
    cached_code = cache.get(f"sms_code_{phone}")
    if cached_code and cached_code == str(code):
        cache.delete(f"sms_code_{phone}")
        return True
    return False