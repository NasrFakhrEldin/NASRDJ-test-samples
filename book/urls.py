from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import IndexView, BookDetailView, GenreView, AddBookView

app_name = "book"

urlpatterns = [
    path('', TemplateView.as_view(template_name = "bookmain.html",
                                    extra_context = {"title":"Samples for book App"})),
    path('index', IndexView.as_view(), name = 'index'),                                
    path('<slug:slug>', BookDetailView.as_view(), name = 'book-detail'),
    path('g/<str:genre>', GenreView.as_view(), name='genre'),
    path('add/', AddBookView.as_view(), name = "add"),
]