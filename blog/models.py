from django.utils import timezone

from django.db import models


# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50, verbose_name='blog_author')

    # this allow the method to be called as a string
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')


@property
def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url
