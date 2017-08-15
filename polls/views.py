
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Question, Choice


class CategoryListView(ListView):

    template_name = 'polls/home.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        return context


class QuestionsView(DetailView):

    model = Category
    template_name = 'polls/ques.html'

    def get_context_data(self, **kwargs):

        context = super(QuestionsView, self).get_context_data(**kwargs)
        context['ques'] = Question.objects.all()
        return context


class QuestionsDetailView(DetailView):
    model = Question
    template_name = 'polls/ques_choice.html'

    def get_context_data(self, **kwargs):

        context = super(QuestionsDetailView, self).get_context_data(**kwargs)
        context['choices'] = Choice.objects.all()
        return context


class ResultView(DetailView):

    template_name = 'polls/results.html'
    model = Choice

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        ques_id = self.kwargs['pk']
        question = get_object_or_404(Question, id=ques_id)

        try:
            selected_choice = question.choice_set.get(pk=self.request.GET.get('choice'))
            context['page'] = Question.objects.get(id=ques_id)
            selected_choice.votes += 1
            selected_choice.save()
            return context
        except Exception:
                context['message'] = "no choice selected "
                return context
