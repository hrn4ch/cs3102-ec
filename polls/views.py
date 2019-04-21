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

def practice(request):
    return render(request, 'polls/practice.html')

"""
def profile(request):
    return render(request, 'housing/profile.html')

def edit_profile(request):
    if request.method == 'POST':
        uform = EditUserForm(request.POST, instance=request.user)
        pform = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
        if uform.is_valid():
            e = uform.cleaned_data['email']
            first = uform.cleaned_data['first_name']
            last = uform.cleaned_data['last_name']
            request.user.email = e
            request.user.first_name = first
            request.user.last_name = last
            request.user.save()
            return redirect('/profile')
    else:
        uform = EditUserForm(instance=request.user)
        pform = EditProfileForm(instance=request.user.profile)
        args = {'uform': uform, 'pform':pform}
        return render(request, 'housing/edit_profile.html', args)
"""