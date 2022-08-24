from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article_update.html"
    fields = (
        "title",
        "body",
    )


class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = (
        "title",
        "body",
        "author",
    )
