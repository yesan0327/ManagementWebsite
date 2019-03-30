from django.shortcuts import render
from papers.models import Paper
from django.core.paginator import Paginator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from papers.models import Paper
from django.db.models import Q


def home(request):
    paper0 = Paper.objects.filter(conference__contains='ASE').filter(time=2013).count()
    paper1 = Paper.objects.filter(conference__contains='ASE').filter(time=2014).count()
    paper2 = Paper.objects.filter(conference__contains='ASE').filter(time=2011).count()
    paper3 = Paper.objects.filter(conference__contains='ASE').filter(time=2007).count()
    return render(request, 'home.html', {'paper0': paper0})


def each(request):
    paper = Paper.objects.filter(_id='5c9eda5cf2fc6b2b728d92a5')
    return render(request, 'paper/each.html',  {'paper': paper})
