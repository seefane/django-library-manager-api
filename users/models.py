from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200,default="https://cdn-icons-png.flaticon.com/512/3135/3135773.png")
    course = models.TextField(max_length=50)
    study_level = models.IntegerField(default=1)
    department_choices = [
        ("education", 'Education'),
        ("computer science", 'Computer Science'),
        ("mathematics", 'Mathematics'),
        ("engineering", 'Engineering'),
    ]
    department = models.CharField(
        max_length=50,
        choices=department_choices,
        default="Education",
    )
    def __str__(self):
        return self.user.username
