from django import forms
from . import models as calification_engine_models
class Calification(forms.ModelForm):

    class Meta:
        model = calification_engine_models.Calification

        fields = (
            'rating',
            'opinion'
        )

        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'rating rating-loading'
            }),
            'opinion': forms.Textarea(attrs={
                'class': 'materialize-textarea'
            })
        }