from django.db import models

from myuser.models import MyUser


class Ticket(models.Model):
    class TicketStatus(models.TextChoices):
        NEW = 'NEW', 'New'
        IN_PROGRESS = "IN_PROGRESS", 'In Progress'
        DONE = "DONE", 'Done'
        INVALID = "INVALID", 'Invalid'

    title = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    created_by = models.OneToOneField(
        MyUser, related_name='MyUser_as_Created_by', on_delete=models.CASCADE)
    status_choices = models.CharField(
        max_length=11, choices=TicketStatus.choices, default=TicketStatus.NEW)
    completed_by = models.OneToOneField(
        MyUser, related_name='MyUser_as_Completed_by', on_delete=models.CASCADE, null=True, blank=True)
