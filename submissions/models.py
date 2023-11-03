# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Submission(models.Model):
    author_name = models.CharField(max_length=255)
    article_name = models.CharField(max_length=255)
    date_submitted = models.DateField()
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
    file_data = models.BinaryField()
    file_url = models.CharField(max_length=255)
    reviewers = models.ManyToManyField(User, related_name='assigned_submissions')



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
        ('Needs Revision', 'Needs Revision'),
    ]
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending'
    )
    comments = models.TextField()

    class Meta:
        app_label = 'submissions'
        db_table = 'reviews'

from django.contrib.auth.models import Group

editors_group, created = Group.objects.get_or_create(name='Editors')
reviewers_group, created = Group.objects.get_or_create(name='Reviewers')
submitter_group, created = Group.objects.get_or_create(name='Submitters')
