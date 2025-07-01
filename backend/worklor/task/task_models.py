import uuid
from django.db import models
from django.conf import settings
from team.team_models import Team


"""
    creating choices for task status
"""

# STATUS_CHOICES = [
#         ('todo', 'To Do'),
#         ('in_progress', 'In Progress'),
#         ('done', 'Done'),
#     ]

class Status(models.TextChoices):
    TODO = 'todo', 'To Do'
    IN_PROGRESS = 'in_progress', 'In Progress'
    DONE = 'done', 'Done'



class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description=models.TextField(blank=True)
    status=models.CharField(
        max_length=50,
        choices=Status.choices,
        default=Status.TODO
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks_assigned'
    )
    assigned_on = models.DateTimeField(auto_now=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tasks')


    def __str__(self):
        return f"{self.title} - {self.status}"



