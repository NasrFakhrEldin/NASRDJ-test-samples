from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Message
from django.contrib.humanize.templatetags.humanize import naturaltime
# Create your views here.



class SendMessage(LoginRequiredMixin, View):
    def get(self ,request):
        results = []
        messages = Message.objects.all().order_by("-created_at")[:10]

        return render(request, "chat/chat.html", {"messages":messages})
    
    def post(self, request):
        message = Message(text = request.POST['message'], owner=request.user)
        message.save()
        return HttpResponseRedirect(reverse('chat:send'))



# class ReceiveMessage(LoginRequiredMixin, View):
#     def get(self ,request):
#         messages = Message.objects.all().order_by("-created_at")[:10]

#         for message in messages:

#             text = message.text
#             time = naturaltime(message.created_at)

#             return render(request, "chat/chat.html", {
#                 "text" : text,
#                 "time" : time
#             })