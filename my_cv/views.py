from django.shortcuts import render
from django.views import generic

# Create your views here.


class MyCV(generic.View):

    @staticmethod
    def index(request):
        return render(request, 'my_cv/index.html', {})