from django import forms

from .models import Category, Question, Choice


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('category', 'question_text', 'pub_date')


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('question', 'choice_text')
