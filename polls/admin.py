from django.contrib import admin


from .models import Question, Choice, Category

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Choice)
