from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime

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

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import Submission

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='./submissions/files/')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        # Create a new submission record in the database
        submission = Submission(article_name=myfile.name, author_name=request.user.username, 
                                file_url=uploaded_file_url, date_submitted=datetime.today().strftime('%Y-%m-%d'))
        submission.save()
        
        return render(request, 'submit.html', {
            'submit': uploaded_file_url
        })
    return render(request, 'submit.html')


