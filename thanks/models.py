from django.db import models
from django.db.models import Model
from django.core.exceptions import ValidationError

# Create your models here.

class Message(models.Model):

  COLOR_CHOICES = [
    ("BL", "Blue"),
    ("RE", "Red"),
    ("YE", "Yellow"),
    ("WH", "White")
  ]

  name = models.CharField(max_length=25, default="Anonymous User")
  content = models.CharField(max_length=300)
  published = models.BooleanField(default=False)
  date_created = models.DateTimeField(auto_now=True)
  color = models.CharField(max_length=2, choices=COLOR_CHOICES, default="BL")

  def __str__(self):
    return self.content

  def set_user(self):
    if(len(self.name) == 0):
      self.name = 'Anonymous User'
  
  def set_color(self):
    if(len(self.color) == 0):
      self.color = "BL"