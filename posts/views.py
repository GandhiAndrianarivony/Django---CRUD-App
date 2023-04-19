# posts/views.py

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView
)
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from posts.models import BlogPost
from posts.forms import BlogPostForm

# Create your views here.

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_delete.html"
    success_url = reverse_lazy("posts:blogpost_list")

class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_detail.html"

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_form.html"
    form_class = BlogPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Update"
        context["article_title"] = "Updating Article"
        return context

class BlogPostView(ListView):
    model = BlogPost
    template_name = "posts/blogpost_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        """User not authenticated can only see published post"""
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs
        return qs.filter(published=True)

@method_decorator(login_required, name='dispatch')
class BlogPostCreateView(CreateView):
    """Only user authenticated can create post"""
    model = BlogPost
    template_name = "posts/blogpost_form.html"
    fields = [
        "title",
        "content",
    ]
    # success_url = reverse_lazy("posts:blogpost_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Create"
        context["article_title"] = "Creating Article"
        return context
