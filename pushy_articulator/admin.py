from models import PushyArticle
from django.contrib import admin
from django import forms
from django.db import models

class PushyArticleAdmin(admin.ModelAdmin):
  formfield_overrides = { models.TextField: { 'widget': forms.Textarea(attrs={'class':'ckeditor'})},}

  class Media:
    js = ('/site_media/js/ckeditor/ckeditor.js',) # The , at the end of this list IS important.
       

admin.site.register(PushyArticle, PushyArticleAdmin)