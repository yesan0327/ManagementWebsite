from django.shortcuts import render
from papers.models import Paper
from django.core.paginator import Paginator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

def home(request):

    return render(request, 'home.html', None)
