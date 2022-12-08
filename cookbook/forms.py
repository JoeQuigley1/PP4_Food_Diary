from .models import Comment, Submission
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
        

class SubmitRecipeForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = (
            'submission_title',
            'ingredients',
            'method',
            'image',
        )

