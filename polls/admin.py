from django.contrib import admin
from .models import Question, Choice
# Register your models here.



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'Question_text']
    inlines = [ChoiceInline]
    list_display = ["Question_text", "pub_date", "was_published_recently"]
    list_filter = ['pub_date']
    search_fields = ['Question_text']




admin.site.register(Question, QuestionAdmin)