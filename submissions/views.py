from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

# Create your views here.

# views.py
from django.shortcuts import render
from .models import Submission
from django.db.models import Q

def submissions(request):
    submissions = Submission.objects.all()
    return render(request, 'submissions.html', {'submissions': submissions})

def search_submissions(request):
    query = request.GET.get('search')
    if query:
        submissions = Submission.objects.filter(
            Q(article_name__icontains=query) | Q(author_name__icontains=query)
        )
    else:
        submissions = Submission.objects.all()
    return render(request, 'submissions.html', {'submissions': submissions})


def index(request):
    return HttpResponse('Hi!')