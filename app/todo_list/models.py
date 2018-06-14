from django.db import models
from django.utils import timezone


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField('completed')
    added_time = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.item}'
