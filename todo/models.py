from django.db import models
from django.urls import reverse
from django.utils import timezone
class todolist(models.Model):
    todoitem=models.CharField(max_length=100)
    done=models.BooleanField(default=False)
    dateposted=models.DateTimeField(default=timezone.now)




    def __str__(self):
        return self.todoitem

    def get_absolute_url(self):
        return reverse('index')
