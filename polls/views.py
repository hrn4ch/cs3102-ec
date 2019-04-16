from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
ListView,
DetailView,
CreateView,
TemplateView
)
from django.utils import timezone

from .models import Topic

class LoginView(TemplateView):
    template_name = 'polls/base.html'

    def post(self, request):
        return HttpResponseRedirect("/topics/")


def list_topics(request):
    topics = Topic.objects.all()
    template_name = 'polls/index.html'
    context = {
        'topics': topics,
    }
    return render(request, template_name, context)


def post_topic(request, topic_title):
    topic = Topic.objects.get(title=topic_title)
    template_name = topic.postURL
    context = {
        'topic': topic,
    }
    return render(request, template_name, context)

