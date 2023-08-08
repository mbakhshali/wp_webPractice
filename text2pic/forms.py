from django import forms

class text2picForm (forms.Form):
    txt = forms.CharField(max_length=250)
    fonts_choices = (
        ('BeautyDemo', 'BeautyDemo'),
        ('BROADW' , 'BROADW'),
        ('Digi Anil Bold', 'Digi Anil Bold'),
    )
    fonts = forms.ChoiceField(choices=fonts_choices)

    color_choices = (
        ('orange', 'orange'),
        ('white', 'white'),
        ('black', 'black'),
        ('red' , 'red'),
        ('green' , 'green'),
        ('yellow' , 'yellow'),
        ('pink', 'pink')
    )
    colors = forms.ChoiceField(choices=color_choices)