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