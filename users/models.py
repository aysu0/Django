from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.png', upload_to = 'profile_pics')


def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}'

def get_absolute_url(self):
    return reverse('itreporting:issue-detail', kwargs = {'pk': self.pk})