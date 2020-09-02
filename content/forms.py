from django import forms

from .models import Feedback

class CommentForm(forms.ModelForm):
    # rate = forms.IntegerField()

    class Meta:
        model = Feedback
        fields = ('comment', 'rate')