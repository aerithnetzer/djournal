from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class SubmitWork(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    first_author_name = forms.CharField(max_length=255)
    agree_to_terms = forms.BooleanField(required=True)

class CreateAccount(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    agree_to_terms = forms.BooleanField(required=True)
    template_name = 'accounts/create_account.html'

class AssignReviewer(forms.Form):
    reviewer1 = forms.CharField(max_length=50)
    reviewer2 = forms.CharField(max_length=50)
    reviewer3 = forms.CharField(max_length=50)
    submission_id = forms.CharField(max_length=50)

    template_name = 'accounts/assign_reviewer.html'

class ReviewSubmission(forms.Form):
    reviewer_name = forms.CharField(max_length=50)
    submission_id = forms.CharField(max_length=50)
    comments = forms.CharField(max_length=1000)
    rating = forms.IntegerField(min_value=1, max_value=5)

    template_name = 'accounts/review_submission.html'