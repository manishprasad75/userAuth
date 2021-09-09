from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.


class OTP(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, unique=False, blank=True, null=True)
    valid_upto = models.DateTimeField(default=datetime.now() + timedelta(minutes=30))


class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_valid = models.BooleanField(default=False)


