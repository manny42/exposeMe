from django.conf.urls import url

from . import views

app_name = 'my_cv'
urlpatterns = [
    url(r'^$', views.MyCV.as_view(), name='index'),
]