# Create your models here.
# models.py

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class Submission(models.Model):
    author_name = models.CharField(max_length=255)
    article_name = models.CharField(max_length=255)
    date_submitted = models.DateField()
    reviewer_1 = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviewer_1', null=True)
    reviewer_2 = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviewer_2', null=True)
    reviewer_3 = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviewer_3', null=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    file_url = models.FileField(upload_to='submissions/')

    class Meta:
        app_label = 'submissions'
        db_table = 'submissions'

class Review(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255)
    date_reviewed = models.DateField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    comments = models.TextField()

    class Meta:
        app_label = 'submissions'
        db_table = 'reviews'