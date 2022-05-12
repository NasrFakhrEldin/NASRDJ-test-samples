from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.

def index(request):
    return HttpResponse('hi')

# class SendMessage(LoginRequiredMixin, View):
