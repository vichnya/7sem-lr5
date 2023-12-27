from django import forms
from .models import Question

class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

    choice_texts = forms.CharField(widget=forms.Textarea)