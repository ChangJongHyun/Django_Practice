from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_list.html'


class BookmarkDV(DetailView):
    model = Bookmark

