from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        unique=True, max_length=128, null=True, blank=True
    )
    birth_date = models.DateField(blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        first_and_last_name = f'{self.first_name} {self.last_name}'
        return self.username if self.username else first_and_last_name


class Order(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='order'
    )
    product = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.user} {self.product}'
