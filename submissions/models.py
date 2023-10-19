# Create your models here.
# models.py

from django.db import models

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
    file_url = models.FileField(upload_to='submissions/')

    class Meta:
        app_label = 'submissions'
        db_table = 'submissions'