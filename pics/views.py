from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from pics.models import Pic
from pics.owner import  OwnerListView, OwnerDetailView, OwnerDeleteView
from django.views.generic import ListView
from .forms import CreateForm
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.

class PicCreateView(LoginRequiredMixin, ListView): # using form not model
    template_name = "pics/form.html"
    success_url = reverse_lazy('pics:all')

    def get(self, request, pk=None):
        form = CreateForm()

        return render(request, self.template_name, {
            "form" : form,
        })

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            return render(request, self.template_name, {
                "form" : form,
            })

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)




class PicListView(OwnerListView):
    model = Pic
    template_name = "pics/list.html"
    success_url = reverse_lazy('pics:all')

class PicDetailView(OwnerDetailView):
    model = Pic
    template_name = "pics/detail.html"
    success_url = reverse_lazy('pics:all')



class PicUpdateView(LoginRequiredMixin, ListView):
    success_url = reverse_lazy('pics:all')
    template_name = "pics/form.html"

    def get(self, request, pk):
        pic = get_object_or_404(Pic, id=pk, owner = self.request.user)
        form = CreateForm(instance=pic)

        return render(request, self.template_name, {
            "form" : form,
        })


    def post(self, request, pk=None):
        pic = get_object_or_404(Pic, id=pk, owner = self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            return render(request, self.template_name, {
                "form" : form,
            })
        
        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)



class PicDeleteView(OwnerDeleteView):
    model = Pic
    template_name = "pics/delete.html"
    success_url = reverse_lazy('pics:all')


def stream_file(request, pk):
    pic = get_object_or_404(Pic, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response