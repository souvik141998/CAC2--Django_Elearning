from django.db import models

# Create your models here.


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    topics_handled = models.TextField()
    contact_no = models.CharField(max_length=15)
