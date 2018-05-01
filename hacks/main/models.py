from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class CollaboratingOrganization(models.Model):
    name = models.CharField(max_length=40)
    text = models.TextField(max_length=500)
    status = models.TextField(max_length=50, default='')
    logo = models.ImageField(upload_to="static", default="static/logo_post.jpg")

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=40)
    text = models.TextField(max_length=500)
    status = models.TextField(max_length=50, default='')
    
    def __str__(self):
        return self.name


class EducationalProject(models.Model):
    name = models.CharField(max_length=40)
    text = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="static", default="static/logo_post.jpg")

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    supporters = models.ManyToManyField(CollaboratingOrganization)

    def __str__(self):
        return self.name


class Employer(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class IndustrialProject(models.Model):
    name = models.CharField(max_length=40)
    text = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="static", default="static/logo_post.jpg")

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Startup(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=500)
    money = models.FloatField()
    sponsors = models.ManyToManyField(Sponsor)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    publication_date = models.DateTimeField('date published')

    logo = models.ImageField(upload_to="static", default="static/logo_post.jpg")
    
    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    start_ups = models.ManyToManyField(Startup)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
