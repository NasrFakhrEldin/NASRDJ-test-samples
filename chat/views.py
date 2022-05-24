from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Message
from django.contrib.humanize.templatetags.humanize import naturaltime
# Create your views here.


class ListSendMessage(LoginRequiredMixin, View):
    
    def get(self, request):
        return render(request, "chat/chat.html")
    
    def post(self, request):
        message = Message(text = request.POST['message'], owner=request.user)
        message.save()
        return redirect(reverse('chat:send'))



class ReceiveMessage(LoginRequiredMixin, View):
    def get(self ,request):
        messages = Message.objects.all().order_by("-created_at")[:10]
        results = []
        
        for message in messages:
            result = [message.text, naturaltime(message.created_at)]
            results.append(result)

        return JsonResponse(results, safe=False)