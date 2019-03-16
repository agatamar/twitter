from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import CreateView

import twitter.forms as forms

from twitter.models import Tweet
# Create your views here.

class TweetListView(generic.ListView):
    template_name = 'twitter/index.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.all().order_by('-creation_date')

class RegisterView(View):
    template_name = 'twitter/register.html'
    form_class = forms.UserRegisterForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('/')

        return render(request, self.template_name, {'form': form})

class ComposeView(LoginRequiredMixin, CreateView):
    model = Tweet
    form_class = forms.TweetForm
    success_url = reverse_lazy('twitter:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)