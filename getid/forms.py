from django import forms
from getid.models import InterestedPerson


class InterestedPersonForm(forms.ModelForm):
    class Meta:
        model=InterestedPerson
        
InterestedPersonForm = InterestedPersonForm
