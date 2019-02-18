from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
ListView,
DetailView,
CreateView,
)
from django.utils import timezone

from .models import Question, Choice, Suggestion

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return  Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

class SuggestionView(CreateView):
    model = Suggestion
    fields = ['name', 'suggestion']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ListView(ListView):
    model = Suggestion
    template_name = 'polls/suggestion_list.html'
    context_object_name = 'suggestions'


def list(request):
    try:
        suggestions = {
            'name': request.POST['name'],
            'suggestion': request.POST['suggestion']
        }
        context = {
            'suggestions': suggestions
        }
    except KeyError:
        return render(request, 'polls/suggestion_form.html', {'error_message': "You didn't make a suggestion.", })
    else:
        return HttpResponseRedirect(reverse('polls:list'),context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question,
                      'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
