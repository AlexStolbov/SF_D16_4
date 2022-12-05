from django.shortcuts import render
from django.views.generic import ListView

from .models import Maker


class MakerList(ListView):
    model = Maker
    template_name = 'maker_list.html'
    context_object_name = 'makers'
