from django import forms
from django.forms import ModelForm
from catalog.choices import *

from catalog.models import PlayerModel, PlayerRegisterModel

class PlayerRegisterForm(ModelForm):
    """Form to record player registration"""
    player_name = forms.ModelChoiceField(queryset=PlayerModel.objects.all(), empty_label='Select name', label='')
    tour_status = forms.ChoiceField(choices=STATUS_OPTIONS, label='')
    comments = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":30}),  label='', required=False)

    class Meta:
            model=PlayerRegisterModel
            fields = ('player_name', 'tour_status', 'comments',)
