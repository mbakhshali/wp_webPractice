from django import forms

class postForm(forms.Form):

    pTitle = forms.CharField(max_length=250)
    pSlug = forms.SlugField(max_length=250)
    pTXT = forms.CharField(widget=forms.Textarea)

