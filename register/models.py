from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(User):
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.username}'
    def verify_checking(self):
        return self.is_verified
    def full_name(self):
        return self.first_name + " " + self.last_name