from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.urls import reverse

from blog.utils import get_read_time, create_slug, create_description


class Album(models.Model):
    """
    this contains list of  spotlight
    """
    name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image

    def get_absolute_url(self):
        return reverse('blog:album', kwargs={'pk': self.pk})


class Spotlight(models.Model):
    """
    this is used to create spotlight
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image


class Post(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True, max_length=500)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    if not instance.description:
        instance.description = create_description(instance.name)


pre_save.connect(pre_save_post_receiver, sender=Post)


class HighLight(models.Model):
    """
    this is used to create spotlight
    """
    name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image
