from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Message
# Create your views here.

def index(request):
    return HttpResponse('hi')

class SendMessage(LoginRequiredMixin, View):
    
    def get(self, request):
        return render(request, ".html")
    
    def post(self, request):
        message = Message(text = request.POST['message'], owner=request.user)
        message.save()
        return redirect(reverse('chat:'))