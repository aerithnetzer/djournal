from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class SubmitWork():
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    first_author_name = forms.CharField(max_length=255)
    agree_to_terms = forms.BooleanField(required=True)

