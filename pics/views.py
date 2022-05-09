from django.shortcuts import render
from django.urls import reverse_lazy
from pics.models import Pic
from pics.owner import OwnerCreateView, OwnerListView, OwnerDetailView, OwnerUpdateView, OwnerDeleteView

# Create your views here.

class PicCreateView(OwnerCreateView):
    model = Pic
    fields = ["title","text","picture"]
    success_url = reverse_lazy('pics:pic-list')


class PicListView(OwnerListView):
    model = Pic
    context_object_name = "pics"
    paginate_by = 4


class PicDetailView(OwnerDetailView):
    model = Pic


class PicUpdateView(OwnerUpdateView):
    model = Pic
    fields = ["title","text","picture"]
    success_url = reverse_lazy('pics:pic-list')


class PicDeleteView(OwnerDeleteView):
    model = Pic
    success_url = reverse_lazy('pics:pic-list')
    template_name = 'pics/pic_delete.html'