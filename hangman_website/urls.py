from django.conf.urls import url

from . import views

app_name = 'hangman_website'
urlpatterns = [
    url(r'^$', views.HangmanView.as_view(), name='index'),
    url(r'^reset/$', views.reset_game, name='reset'),
]