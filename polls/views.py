
from django.http import HttpResponseRedirect, HttpResponse
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
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





# def get_context_data(self, **kwargs):
#             context = super(ResultDisplayView, self).get_context_data(**kwargs)
#             ques_id = self.kwargs['pk']
#             question = get_object_or_404(Question, id=ques_id)
#             try:
#                 selected_choice = question.choice_set.get(id=self.request.GET['choice'])

#                 context['page']=Question.objects.get(id =ques_id)
#                 selected_choice.votes += 1
#                 selected_choice.save()
#                 return context
#             except Exception :
#                 context['message'] = "no choice selected "
#                 return context































# class ResultDisplayView(DetailView):


#     template_name = 'poll/display_result.html'
#     model = Choice

#     def get_context_data(self, **kwargs):

#         context = super(ResultDisplayView, self).get_context_data(**kwargs)
#         ques_id = self.kwargs['pk']
#         print(ques_id)

#         context['page']=Question.objects.get(id =ques_id)
#         page =  Question.objects.get(id =ques_id)
#         n =page.choice_set.all()
#         for u in n:
#             u.votes = u.votes +1
#             u.save()












    # def post(self,request, question_id):
    #     question = get_object_or_404(Question, pk=question_id)

    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     return HttpResponse('result')
    #     return super(Api, self).dispatch(request, *args, **kwargs)

    # # def get_context_data(self, **kwargs):

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





































