from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Decision(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True, null=True)
    pros = models.JSONField(default=list, blank=True, null=True)
    cons = models.JSONField(default=list, blank=True, null=True)