from django.shortcuts import render

from base import views as base_views

from . import models as rating_engine_models
from . import forms as rating_engine_forms
# Create your views here.


class Rate(base_views.BaseCreateView):
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
        return self.get_success_url()


