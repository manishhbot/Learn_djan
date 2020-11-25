from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models


# Create your views here.

class SchoolListView(ListView):
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = "ListView/school_detail.html"
