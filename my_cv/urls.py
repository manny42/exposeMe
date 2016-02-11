from django.conf.urls import url
from django.views.generic import TemplateView

app_name = 'my_cv'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='my_cv/index.html')),
]