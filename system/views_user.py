from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

class IndexView(View):

    def get(self, request):
        return render(request, 'system/index.html')