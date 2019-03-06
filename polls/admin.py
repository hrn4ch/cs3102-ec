from django.contrib import admin
from .models import Question, Choice, Suggestion

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':
                              ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class SuggestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['suggestion']}),
    ]
    list_display = ('name','suggestion')

admin.site.register(Suggestion, SuggestionAdmin)

admin.site.register(Question, QuestionAdmin)
