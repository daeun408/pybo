from django.db import models

# Create your models here.

class Diary(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()

class Todolist(models.Model):
    todo = models.CharField(max_length=200)
    end_date = models.DateField()
    done = models.BooleanField()

