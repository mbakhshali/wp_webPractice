from django import forms


class ReportForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    subject_choices = (
        ('Bug', 'Bug'),
        ('Suggestions', 'Suggestions')
    )
    subject = forms.ChoiceField(choices=subject_choices)