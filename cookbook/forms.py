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
            'submission_slug',
            'ingredients',
            'method',
            'image',
        )

        labels = {
            'submission_title': 'Recipe name',
            'submission_slug': 'Repeat name without spaces',
            'ingredients': 'Ingredients',
            'method': 'Method',
            'image': 'Recipe Image',
        }

