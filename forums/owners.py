from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



class OwnerCreateView(LoginRequiredMixin, CreateView):

    ''' OwnerCreateView '''
    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)


class OwnerListView(ListView):
    ''' OwnerListView '''


class OwnerDetailView(DetailView):
    ''' OwnerDetailView '''


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    ''' OwnerUpdateView '''

    def get_queryset(self):
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner = self.request.user)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    ''' OwnerDeleteView '''

    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner = self.request.user)

