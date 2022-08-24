from django.urls import path
from .views import *

urlpatterns = [
    path("", ArticlesListView.as_view(), name="articles_list"),
]
