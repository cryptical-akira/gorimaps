from django import forms
from django.contrib import admin
from django.forms import models
from django.forms.widgets import Textarea

# Register your models here.
from .models import MultilanguageText, MultilanguageLongText, \
    MultilanguageTextField


class MultilanguageLongTextAdminForm(forms.ModelForm):
    text_en = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,
                                                           'cols': 100,
                                                           'style': 'height: 4em;'}))
    text_ka = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,
                                                           'cols': 100,
                                                           'style': 'height: 4em;'}))
    class Meta:
        model = MultilanguageLongText
        fields = ['text_en', 'text_ka']


@admin.register(MultilanguageText)
class MultilanguageTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_en', 'text_ka')
    list_editable = ('text_en', 'text_ka')
    fields = ['text_en', 'text_ka','slug']


@admin.register(MultilanguageLongText)
class MultilanguageLongTextAdmin(admin.ModelAdmin):
    form = MultilanguageLongTextAdminForm
    list_display = ('id', 'text_en', 'text_ka')
    list_editable = ('text_en', 'text_ka')    


@admin.register(MultilanguageTextField)
class MultilanguageTextFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'text_en_intro', 'text_ka_intro')
    list_editable = ('slug', )