from django.shortcuts import render
from django.views.generic import TemplateView , DeleteView, ListView, FormView, CreateView
from .models import Books
from .forms import AddForm
from django.db.models import F
from django.utils import timezone
# Create your views here.

# class IndexView(TemplateView):
#     template_name = "home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = Books.objects.all()
#         return context

# class AddBookView(FormView):
#     template_name = "add.html"
#     form_class = AddForm
#     success_url = "/book/"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class AddBookView(CreateView): # using Createview instead of Formview
    model = Books
    template_name = "add.html"
    fields = ['title', 'genre', 'author', 'isbn'] # working here
    # form_class = AddForm # and here
    success_url = "/book/"

    # def get_initial(self, *args, **kwargs): # it is a different way of working here to widgets -initial-
    #     initial = super().get_initial(**kwargs)
    #     initial['title'] = "Enter Title"
    #     initial['genre'] = "Enter Genre"
    #     return initial


class IndexView(ListView):
    model = Books
    template_name = "home.html"
    context_object_name = "books" # you should know what is the defualt value for this
    #this should be work with out change it thing in the class above
    paginate_by = 4 # got to html for this class to add back and forward arrow - show the doc for this
    # queryset = Books.objects.all()[:2]

    def get_queryset(self):
        # return Books.objects.all()[:3] # the same operations
        return Books.objects.all()


class GenreView(ListView):
    model = Books
    template_name = "home.html"
    context_object_name = "books" 
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        return Books.objects.filter(genre__icontains = self.kwargs.get('genre')) # __icontains for case sensitive



class BookDetailView(DeleteView):
    model = Books
    template_name = "book-detail.html"
    context_object_name = 'book'

    # you can add it from models.py
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Books.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)
        context['time'] = timezone.now()

        return context
