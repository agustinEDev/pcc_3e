from django import forms

from .models import Blog, BlogEntry

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']
        labels = {'title': '', 'description': 'Descripción:'}

class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['title', 'text']
        labels = {'title': '', 'text': 'Texto:'}
        widgets = {'text': forms.Textarea(attrs = {'cols': 80})}