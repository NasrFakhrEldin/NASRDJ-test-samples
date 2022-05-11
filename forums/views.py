from .owners import *
from .models import Forum, Comment
from django.urls import reverse, reverse_lazy
from .forms import CommentForm
from django.shortcuts import render
# Create your views here.


class ForumCreateView(OwnerCreateView): # using model not form as pics app
    model = Forum
    template_name = 'forums/form.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('forums:all')

class ForumListView(OwnerListView):
    model = Forum
    template_name = 'forums/list.html'


class ForumDetailView(OwnerDetailView):
    model = Forum
    template_name = 'forums/detail.html'

    def get(self, request, pk):
        forum = Forum.objects.get(id=pk)
        comments = Comment.objects.filter(forum=forum).order_by('-updated_at')
        comment_form = CommentForm()
        return render(request, self.template_name, {
            "forum" : forum,
            "comments" : comments,
            "comment_form" : comment_form,
        })


class ForumUpdateView(OwnerUpdateView):
    model = Forum
    template_name = 'forums/form.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('forums:all')

class ForumDeleteView(OwnerDeleteView):
    model = Forum
    template_name = 'forums/delete.html'
    success_url = reverse_lazy('forums:all')