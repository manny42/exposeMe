from django.shortcuts import render

# Create your views here.

class MyCV():

    def index(self, request):
        return render(request, 'my_cv/index.html')