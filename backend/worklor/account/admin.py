from django.contrib import admin
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user_profile.profile_models import UserProfile

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):

    ordering = ['email']
    list_display = ['email', 'full_name', 'is_active', 'is_staff']
    search_fields = ['email', 'full_name']
    readonly_fields = ['joining_date', 'updated_at']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('full_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'updated_at', 'joining_date')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.register(UserProfile)
