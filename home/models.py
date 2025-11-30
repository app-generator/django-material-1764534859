# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Project(models.Model):

    #__Project_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Task(models.Model):

    #__Task_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    priority = models.CharField(max_length=255, null=True, blank=True)
    due_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Task_FIELDS__END

    class Meta:
        verbose_name        = _("Task")
        verbose_name_plural = _("Task")


class Timeentry(models.Model):

    #__Timeentry_FIELDS__
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    duration = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Timeentry_FIELDS__END

    class Meta:
        verbose_name        = _("Timeentry")
        verbose_name_plural = _("Timeentry")



#__MODELS__END
