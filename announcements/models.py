from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Announcements(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='announcement_posts')
    lastupdated = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-lastupdated']

    def __str__(self):
        return self.title
