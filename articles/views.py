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
from .forms import CommentForm


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["form"] = CommentForm()
        return context


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.use


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "article_update.html"
    fields = (
        "title",
        "body",
    )

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.use


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
