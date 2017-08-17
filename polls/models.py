from django.db import models
from django.utils import timezone
import datetime


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        yesterday = now - datetime.timedelta(days=1)
        return now >= self.pub_date >= yesterday


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
