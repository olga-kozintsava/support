from django.contrib.auth import get_user_model
from django.db import models


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
    task = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.author.username} - {self.created_at.strftime("%d/%m/%Y %H:%M:%S")}'
