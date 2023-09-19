from django.db import models
from django.utils import timezone
from django.urls import reverse
from django import forms
# Create your models here.
class Post(models.Model):
  UPTION = [
      ("private","Private"),
      ("public","Public"),
  ]
  publish = models.DateTimeField(default=timezone.now)
  def get_absolute_url(self):
    return reverse("pages:post_details",
	      args = [
	          self.publish.year,
	          self.publish.month,
	          self.publish.day,
	          self.slug,
	        ]
	    )
  title = models.CharField(max_length=100,default="")
  body = models.TextField(default="")
  slug = models.SlugField(max_length=100,unique_for_date="publish",default="")
  image = models.ImageField(upload_to="static/img", default="")
  uptions = models.CharField(max_length=10,
				choices=UPTION,
				default='public')
	
  class Meta:
    ordering = ("-publish",)
  def __str__(self):
    return self.title

class Users(models.Model):
   username = models.CharField(max_length=100,default="  ")
   email = models.CharField(max_length=222,default=" ")
   password = models.CharField(max_length=18,default="")
   confirm_password = models.CharField(max_length=18,default="")
   register_date = models.DateTimeField(default=timezone.now)

class Meta:
    def __str__(self):
        return self.email


class Json(models.Model):
  title = models.CharField(max_length=200)
  body = models.CharField(max_length=100)
class Meta:
  def __str__(self):
    return self.title




