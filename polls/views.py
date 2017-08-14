
from django.http import HttpResponseRedirect
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Category, Question, Choice
from django.urls import reverse


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


class ResultView(TemplateView):
    template_name = 'polls/results.html'
    model = Choice

    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)

        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
        context = {

            'choices': Choice.objects.all(),

        }
        return super(TemplateView, self).render_to_response(context)


    # def get_context_data(self, **kwargs):

    #     context = super(ResultView, self).get_context_data(**kwargs)
    #     context['choices'] = Choice.objects.all()
    #     return context










# def vote(request, question_id):
#     print("**************************************88")
#     question = get_object_or_404(Question, pk=question_id)
#     print("hellow")
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/ques_choice.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id)))


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})





































