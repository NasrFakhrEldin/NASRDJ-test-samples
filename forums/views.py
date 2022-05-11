from .owners import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Forum, Comment
from django.urls import reverse, reverse_lazy
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
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
        comments = Comment.objects.filter(forum = forum).order_by('-updated_at')
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


class CommentCreateView(OwnerCreateView):
    def post(self, request, pk):
        forum = get_object_or_404(Forum, id=pk)
        comment = Comment(forum = forum, owner = self.request.user, text = request.POST['comment']) # text from form
        comment.save()
        return redirect(reverse('forums:forum_detail', args=(pk,)))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = 'forums/comment_delete.html'
    # success_url = reverse_lazy('forums:all')

    # this is the power of OOP
    def get_success_url(self):
        forum = self.object.forum # object.forum => model => class Comment => forum ^_^
        return reverse('forums:forum_detail', args=(forum.id,))