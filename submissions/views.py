from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

# views.py
from django.shortcuts import render
from .models import Submission
from django.db.models import Q

from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.groups.filter(name='Editor').exists())
def restrict_submissions(request):
    submissions=Submission.objects.all()
    return render(request, 'submissions.html', {'submissions':submissions})


@login_required(login_url='/accounts/login/')
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

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
        logout(request)
        return redirect('login')


def home(request):
    return render(request, 'home.html')