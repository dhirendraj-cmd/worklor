import uuid
from django.db import models
from django.conf import settings


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="teams_created"
    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="Membership",
        related_name="member_teams"

    )

    def __str__(self):
        return self.team_name
    


# membership class
class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(default="member", max_length=50)

    """
        User can join same team only once so UniqueConstraint helps in that preventing duplicate joins
    """

    class Meta:
        app_label = 'team'
        constraints = [
            models.UniqueConstraint(fields=['user', 'team'],
                                    name='user_team_one_time_entry_membership') # preventing duplicate joins/entries for same user in same team
        ]
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"
    
    def __str__(self):
        return f"{self.user.email} in {self.team.team_name}"



