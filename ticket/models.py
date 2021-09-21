from django.contrib.auth import get_user_model
from django.db import models
from support import settings


class Ticket(models.Model):

    class TicketStatus(models.TextChoices):
        SOLVED = 'solved'
        UNSOLVED = 'unsolved'
        FROZEN = 'frozen'

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=8,
        choices=TicketStatus.choices,
        default=TicketStatus.UNSOLVED
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
