from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from .models import Article


class ArticlesListView(ListView):
    model = Article
    template_name = "articles_list.html"
