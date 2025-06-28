from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email must be provided!"))
        
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not password:
            raise ValueError(_("Password is required for Superusers!"))
        
        if not extra_fields.get('is_staff'):
            raise ValueError(_('is_staff must be true for Superusers, make is_staff=True'))
        if not extra_fields.get('is_superuser'):
            raise ValueError(_('is_superuser must be true for Superusers, make is_superuser=True'))
        
        return self.create_user(email, password, **extra_fields)


