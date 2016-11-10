from django.shortcuts import render
from django import http

from base import views as base_views

from . import models as rating_engine_models
from . import forms as rating_engine_forms
# Create your views here.


class Rate(base_views.BaseCreateView):
    template_name = "rating_engine/calification/create.html"
    model = rating_engine_models.Calification
    form_class = rating_engine_forms.Calification

    def get_object(self):
        return None

    def get_success_url(self):
        return None


    def form_valid(self, form):
        calification = form.save(commit=False)
        content_object = self.get_object()
        calification.content_object = content_object
        calification.save()
        return http.HttpResponseRedirect(self.get_success_url())


