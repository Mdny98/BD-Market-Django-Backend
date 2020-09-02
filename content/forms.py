from django import forms

from .models import Feedback

class CommentForm(forms.ModelForm):
    # rate = forms.ChoiceField()

    class Meta:
        model = Feedback
        fields = ('comment', 'rate')

# class SearchForm(forms.Form):
#     search = forms.CharField(required=False,
#                              widget=forms.TextInput(attrs={'size': '40'}))