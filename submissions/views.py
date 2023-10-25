from django.template import loader
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Submission
from django.db.models import Q
from .models import Submission
from submissions.forms import CreateAccount
from datetime import datetime
from django.contrib.auth.models import Group

def index(request):
    return render(request, 'index.html')

@user_passes_test(lambda u: u.groups.filter(name='Editors').exists())
def restrict_submissions(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    else:
        return render(request, 'submissions.html', {'submissions':submissions})

@login_required(login_url='/accounts/login/')
def submissions(request):
    submissions = Submission.objects.all()
    print(len(submissions))
    return render(request, 'submissions.html', {'submissions':submissions})

def search_submissions(request):
    query = request.GET.get('search')
    if query:
        submissions = Submission.objects.filter(
            Q(article_name__icontains=query) | Q(author_name__icontains=query)
        )
    else:
        submissions = Submission.objects.all()
    return render(request, 'submissions.html', {'submissions': submissions})


def logout_view(request):
        logout(request)
        return redirect('accounts/login')

@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name = 'Submitters').exists())
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
        
        return render(request, 'submit/confirm_submission.html', {
            'submit': uploaded_file_url
        })
    return render(request, 'submit/upload.html')

@user_passes_test(lambda u: u.groups.filter(name='Reviewers').exists())
def review_submission(request):
    submissions = Submission.objects.all()
    return render(request, 'review.html', {'submissions': submissions})

from django.http import HttpResponse

def confirm_submssion(request):
    return render(request, 'submit/confirm_submission.html')

def submit(request):
    return render(request, 'submit/submit.html')

# View that allows a user to see all of their submissions - look up by username
def my_submissions(request):
    submissions = Submission.objects.filter(author_name=request.user.username)
    return render(request, 'my_submissions.html', {'submissions': submissions})

def create_account(request):
    if request.method == 'POST':
        form = CreateAccount(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            user.save()
            group = Group.objects.get(name='Submitters')
            user.groups.add(group)
            return redirect('my_submissions')
        else:
            form = CreateAccount()
            return render(request, 'accounts/create_account.html', {'form': form})
    else:
        form = CreateAccount()
        return render(request, 'accounts/create_account.html', {'form': form})