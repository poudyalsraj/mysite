from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [

    url(r'^$', views.CategoryListView.as_view(), name='home'),
    url(r'^add/category/$', views.CategoryCreateView.as_view(), name='add-category'),
    url(r'^(?P<pk>\d+)/add/ques/$', views.QuestionCreateView.as_view(), name='add-ques'),
    url(r'^(?P<pk>\d+)/add/choice/$', views.ChoiceCreateView.as_view(), name='add-choice'),
    url(r'^(?P<pk>\d+)/ques/delete/', views.QuestionDeleteView.as_view(), name='ques-del'),
    url(r'^(?P<pk>\d+)/$', views.QuestionsView.as_view(), name='ques'),
    url(r'^ques-all/$', views.AllQuestionView.as_view(), name='all-ques'),

    url(r'^(?P<c_id>\d+)/(?P<pk>\d+)$', views.QuestionsDetailView.as_view(), name='ques-choice'),

    url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='result'),


    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
