from django.shortcuts import render
from django.views import View, generic

from twitter.models import Tweet
# Create your views here.

class TweetListView(generic.ListView):
    template_name = 'twitter/index.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.all().order_by('-creation_date')