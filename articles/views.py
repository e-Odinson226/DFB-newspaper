from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "article_update.html"
    fields = (
        "title",
        "body",
    )


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
