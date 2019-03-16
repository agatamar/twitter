from django.urls import path

from django.views import generic
from twitter import views

app_name = 'twitter'
urlpatterns = [
    # path('', generic.TemplateView.as_view(template_name='twitter/index.html'),
    #      name='index'),
    path('', views.TweetListView.as_view(),
         name='index'),

]