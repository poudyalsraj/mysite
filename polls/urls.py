from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [

    url(r'^$', views.CategoryListView.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', views.QuestionsView.as_view(), name='ques'),

    url(r'^(?P<c_id>\d+)/(?P<pk>\d+)$', views.QuestionsDetailView.as_view(), name='ques-choice'),

    url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='result'),


    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
