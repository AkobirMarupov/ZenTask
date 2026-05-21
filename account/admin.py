from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'phone', 'role', 'is_confirmed', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Shaxsiy ma\'lumotlar', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Ruxsatlar', {'fields': ('role', 'is_active', 'is_staff', 'is_confirmed', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'phone', 'role', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )

    search_fields = ('email', 'first_name', 'last_name', 'phone')
    ordering = ('email',)