from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView
from .views import *
app_name = "CBV"

urlpatterns = [
    path('', TemplateView.as_view(template_name = "main.html",
                                    extra_context = {"title":"Samples for CBV App"})),

    path('postlist', views.PostList.as_view(), name = "postlist"),
    path('extwo', Ex2View.as_view(), name = "extwo"),
    path('rdt', RedirectView.as_view(url = "https://www.youtube.com/"), name = "go-to-very"),
    path('exthree/<int:pk>/', PostPreLoadTaskView.as_view(), name='redirect-task'),
    path('exfour/<int:pk>/', SinglePostView.as_view(),
         name='singlepost'),  # single post page
]