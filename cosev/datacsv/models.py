from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class CsvFile(models.Model):
    title = models.TextField(verbose_name='Title', max_length=150)
    cover = models.FileField(upload_to='file/')
    description = models.TextField(max_length=500)
    date_published = models.DateTimeField(verbose_name='Date published', auto_now_add=True)

    def __str__(self):
        return self.title
