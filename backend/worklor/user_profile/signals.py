from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import User
from .profile_models import UserProfile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


