from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    available_quantity = models.IntegerField()
    max_days_available = models.IntegerField(default=1)
    book_cover = models.CharField(max_length=200)
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
        return self.title

    def increment(self):
        self.available_quantity +=1
    def decrement(self):
        self.available_quantity -=1

class ReservedBook(models.Model):
    reserved_book = models.ForeignKey(Book,on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now() +timedelta(1))
    returned_date=models.DateTimeField(default=timezone.now() +timedelta(1))
    IS_BookNumber = models.CharField(max_length=50,null=True)
    status_choices = [
        ('collection pending','Collection Pending'),
        ("outstanding","Outstanding"),
        ("returned","Returned"),
        ("return pending","Return Pending")]
    status = models.CharField(
    max_length=50,
    choices=status_choices,
    default="outstanding",
    )

