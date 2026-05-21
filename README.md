# 🎓 EduPlatform — LMS & Career Portal Backend

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.17-red?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-Django_Channels-green?style=for-the-badge)

**O'quv markazlari, o'qituvchilar va talabalar uchun keng qamrovli LMS va karyera platformasi.**

</div>

---

## 📌 Loyiha haqida

**EduPlatform** — bu ta'lim olish, kurslarni boshqarish va ish topishni birlashtiradigan backend tizimi. Vakansiyalar markazi va kurs boshqaruvi bir platformada jamlangan.

---

### 🎓 Kurslar va Ta'lim
- Kurslarni yaratish, tahrirlash, o'chirish (CRUD)
- Talabalar kurslarga ariza yuborish tizimi
- Ko'p bosqichli kurs va modul boshqaruvi

### 💼 Vakansiyalar Markazi (SkillSwap)
- Ish beruvchilar uchun vakansiyalar yaratish
- Nomzodlar va ish beruvchilar o'rtasida to'g'ridan-to'g'ri chat
- Arizalarni kuzatish tizimi

### 🔐 Autentifikatsiya
- JWT (JSON Web Token) asosida xavfsiz autentifikatsiya
- `python-decouple` orqali muhit o'zgaruvchilari boshqaruvi

---

## 🛠 Texnologiyalar

| Kategoriya | Texnologiya |
|---|---|
| **Backend** | Python 3.x, Django 6.0 |
| **REST API** | Django REST Framework 3.17 |
| **Ma'lumotlar bazasi** | PostgreSQL (production), SQLite (dev) |
| **Caching / Channels Layer** | Redis |
| **Autentifikatsiya** | JWT (`djangorestframework-simplejwt`) |
| **API Docs** | Swagger / Redoc |
| **Media** | Pillow |
| **Muhit** | Linux (Ubuntu) |

---

## 📂 Loyiha strukturasi

```
EduPlatform/
├── config/             # Asosiy sozlamalar (settings, urls, asgi)
├── account/            # Foydalanuvchi modeli va autentifikatsiya
├── conversation/       # Real-time chat, xabarlar va media fayllar
├── event/              # Kurslar, modullar va ta'lim jarayoni
├── vacancies/          # Vakansiyalar va ish ariza tizimi
├── common/             # Umumiy yordamchi funksiyalar
├── manage.py
├── requirements.txt
└── .env.example
```

---

## 🔌 API Endpointlar

### Auth
| Method | Endpoint | Tavsif |
|--------|----------|--------|
| `POST` | `/api/auth/register/` | Ro'yxatdan o'tish |
| `POST` | `/api/auth/login/` | Login — JWT token olish |
| `POST` | `/api/auth/token/refresh/` | Tokenni yangilash |

### Kurslar
| Method | Endpoint | Tavsif |
|--------|----------|--------|
| `GET` | `/api/events/` | Barcha kurslar |
| `POST` | `/api/events/` | Yangi kurs yaratish |
| `GET` | `/api/events/{id}/` | Kurs tafsiloti |
| `PUT` | `/api/events/{id}/` | Kursni tahrirlash |
| `DELETE` | `/api/events/{id}/` | Kursni o'chirish |

### Vakansiyalar
| Method | Endpoint | Tavsif |
|--------|----------|--------|
| `GET` | `/api/vacancies/` | Barcha vakansiyalar |
| `POST` | `/api/vacancies/` | Yangi vakansiya |
| `GET` | `/api/vacancies/{id}/` | Vakansiya tafsiloti |
---

## ⚙️ O'rnatish

### 1. Reponi klonlash
```bash
git clone https://github.com/AkobirMarupov/ZenTask.git
cd ZenTask
```

### 2. Virtual muhit
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Kutubxonalar
```bash
pip install -r requirements.txt
```

### 4. Muhit o'zgaruvchilari
`.env.example` faylini `.env` ga ko'chiring va to'ldiring:
```bash
cp .env.example .env
```

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/eduplatform
REDIS_URL=redis://localhost:6379
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Migratsiyalar
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Serverni ishga tushirish
```bash
python manage.py runserver
```

API docs: `http://localhost:8000/swagger/`

---

## 👨‍💻 Muallif

**Akobir Marupov** — Python Backend Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/akobir-marupov-55b528401/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AkobirMarupov)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/uvent_1)

---

<div align="center">
⭐ Agar loyiha yoqqan bo'lsa, star bosing!
</div>