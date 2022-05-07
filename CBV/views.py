from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from django.db.models import F

# CBV
from django.views.generic import ListView, TemplateView, RedirectView

# Create your views here.

class PostList(ListView):
    model = Post


class Ex2View(TemplateView):

    template_name = "extwo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] =  Post.objects.get(id=1)
        context['data'] = "Context Data for Ex2"
        return context


class PostPreLoadTaskView(RedirectView):
    # url = "https://www.youtube.com/"
    pattern_name = "CBV:singlepost"
    # permanent = Http status code returned (True = 301, False = 302, Default = False)

    def get_redirect_url(self, *args, **kwargs):
        # post = get_object_or_404(Post, pk=kwargs['pk'])
        # post.count = F('count') + 1
        # post.save()

        post = Post.objects.filter(pk=kwargs['pk'])
        post.update(count=F('count') + 1)

        return super().get_redirect_url(*args, **kwargs)


class SinglePostView(TemplateView):
    template_name = "exfour.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(Post, pk = self.kwargs.get('pk'))
        return context