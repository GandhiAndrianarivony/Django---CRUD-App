# posts/forms.py

from django import forms
from posts.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "published",
            "content"
        ]
        widgets = {
            "content": forms.Textarea()
        }