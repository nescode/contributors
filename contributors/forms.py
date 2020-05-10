from django import forms


ROLE_CHOICES = (
    ('developer', 'as a developer'),
    ('designer', 'as a designer'),
    ('documentation team', 'as a documentation team'),
)


class ContributeForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone = forms.CharField(max_length=13)
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=ROLE_CHOICES)
    about = forms.CharField(max_length=255)
    resume = forms.FileField()
