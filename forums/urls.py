from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('', views.ForumListView.as_view(), name = 'all'),
    path('create', views.ForumCreateView.as_view(), name = 'forum_create'),
    path('<int:pk>', views.ForumDetailView.as_view(), name = 'forum_detail'),
    path('<int:pk>/update', views.ForumUpdateView.as_view(), name = 'forum_update'),
    path('<int:pk>/delete', views.ForumDeleteView.as_view(), name = 'forum_delete'),
    path('<int:pk>/comment', views.CommentCreateView.as_view(), name = 'forum_comment_create'),
]