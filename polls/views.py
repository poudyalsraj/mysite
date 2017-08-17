
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Category, Question, Choice
from .forms import CategoryForm, QuestionForm, ChoiceForm
from django.core.urlresolvers import reverse_lazy, reverse


class CategoryCreateView(CreateView):
        template_name = 'polls/category_form.html'
        form_class = CategoryForm
        success_url = reverse_lazy('polls:home')


class CategoryListView(ListView):
    template_name = 'polls/home.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        return context


class AllQuestionView(ListView):

    """
    Display all questions in the list
    """
    template_name = 'polls/all_ques.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):

        return Question.objects.order_by('-pub_date')


class QuestionsView(DetailView):

    model = Category
    template_name = 'polls/ques.html'

    def get_context_data(self, **kwargs):

        context = super(QuestionsView, self).get_context_data(**kwargs)
        context['ques'] = Question.objects.all()
        return context


class QuestionCreateView(CreateView):
    template_name = 'polls/question_add.html'
    form_class = QuestionForm

    def get_initial(self):

        initials = super().get_initial()
        initials['category'] = self.kwargs['pk']
        return initials

    def get_success_url(self):
        print(self.object.id)
        return reverse('polls:add-choice', args=(self.object.id,))


class QuestionsDetailView(DetailView):
    model = Question
    template_name = 'polls/ques_choice.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionsDetailView, self).get_context_data(**kwargs)
        context['choices'] = Choice.objects.all()
        return context


class QuestionDeleteView(DeleteView):
    model = Question

    def get_success_url(self):
        return reverse('polls:ques', args=(self.object.category.id,))


class ChoiceCreateView(CreateView):
    template_name = 'polls/choice_add.html'
    form_class = ChoiceForm

    def get_initial(self):

        # this get_initial method will auto select the question
        initials = super().get_initial()
        initials['question'] = self.kwargs['pk']
        return initials

    def get_success_url(self):
        return reverse('polls:ques', args=(self.object.question.category.id,))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     new = int(self.kwargs['pk'])
    #     k = Question.objects.get(id=new)
    #     cat = k.category
    #     p = int(cat.id)
    #     print(p)
    #     context['p'] = p

    #    # print(category,"hello")
    #     context['ques'] = self.kwargs['pk']
    #    # print(self.kwargs['pk'])
    #     #print(self.object)
    #     # l = k.category
    #     # print(l)
    #     # print(l.id)
    #     # context['category'] = self.object.question.category.id
    #     return context


class ResultView(DetailView):
    """
    Result Detail ---
    """

    template_name = 'polls/results.html'
    model = Choice

    def get_question(self, **kwargs):
        ques_id = self.kwargs['pk']
        question = get_object_or_404(Question, id=ques_id)
        return question

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        question = self.get_question()
        try:
            selected_choice = question.choice_set.get(pk=self.request.GET.get('choice'))
            context['page'] = question
            selected_choice.votes += 1
            selected_choice.save()
            return context
        except Exception:
            context['message'] = "no choice selected "
            return context
