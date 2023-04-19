# posts/urls.py

from django.urls import path
from posts.views import (
    BlogPostView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDetailView,
    BlogPostDeleteView
)

app_name = "posts"

urlpatterns = [
    path("", BlogPostView.as_view(), name="blogpost_list" ),
    path("create/", BlogPostCreateView.as_view(), name="blogpost_form"),
    path("update/<str:slug>", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("detail/<str:slug>", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path("delete/<str:slug>", BlogPostDeleteView.as_view(), name="blogpost_delete")
]