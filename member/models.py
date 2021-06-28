from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin

class Profile(models.Model):
    REQUIRED_FIELDS = ["user",]
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(max_length=500, blank=True)
    web_page = models.URLField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    job_range = [("Architect","Architect"),("Lecturer/Student","Lecturer/Student"),("Constructor","Constructor"),("Other","Other")]
    job = models.CharField(max_length=30, blank=True, choices=job_range)
    profile_pic = models.ImageField(blank=True, upload_to="uploads/")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Architect(models.Model):
    user = models.OneToOneField(User, related_name='architect', primary_key=True,on_delete=models.CASCADE)
    office = models.CharField(max_length=30, blank=True)
    experience = models.IntegerField(blank=True)

class Constructor(models.Model):
    user = models.OneToOneField(User, related_name='constructor', primary_key=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=30, blank=True)

class Education(models.Model):
    user = models.OneToOneField(User, related_name='education', primary_key=True, on_delete=models.CASCADE)
    university = models.CharField(max_length=30, blank=True)
    role_range = [("Studend", "Student"), ("Post Graduate", "Post Graduate"), ("Phd", "Phd"),("Professor", "Professor")]
    role= models.CharField(max_length=30, blank=True, choices=role_range)
