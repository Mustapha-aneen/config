from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
class PostJob(models.Model):
  OPTIONS = [
      ("Private",'private'),
      ("Public","public")
    ]
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length = 220,
                  unique_for_date = "publish"
          )
  author = models.ForeignKey(User,
            related_name = "jobs_postjob",
            on_delete = models.CASCADE,
            )
  publish = models.DateTimeField(default=timezone.now)
  body = models.TextField()
  status = models.CharField(max_length=200,
                default="public",
                choices = OPTIONS
            )
  def get_absolute_url(self):
    return reverse("jobs:jobs_form_view",
        args = [
            self.slug
          ]
    )
  class Meta:
    ordering = ('-publish',)
  def __str__(self):
    return f"{self.title} posted by {self.author}"
# Create your models here.
class Comment(models.Model):
  job = models.ForeignKey(PostJob,
        related_name = "comments",
        on_delete = models.CASCADE
    )
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)
  class Meta:
    ordering = ("created",)
  def __str__(self):
    return self.name
class Applicant(models.Model):
  firstname = models.CharField(max_length=200)
  lastname = models.CharField(max_length=200)
  job = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  date = models.DateField(default=timezone.now)
  class Meta:
    pass
  def __str__(self):
    return f"{self.firstname} required for a {self.job}"