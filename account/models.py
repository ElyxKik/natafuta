from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AgentUser(AbstractUser):
    is_admin = models.BooleanField(default=False)