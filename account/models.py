from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    date_of_joining = models.DateField(auto_now_add=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.user.username