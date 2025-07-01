import uuid
from django.db import models

from .account_manger import CustomUserManager
from team.team_models import Team, Membership

from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    
    # many to many relation with teams
    teams = models.ManyToManyField("team.Team", through='team.Membership', related_name='team_users')

    # custom manager
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser




