from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

class PostLV(ListView) :
    model = Post

class PostDV(DetailView) :
    model = Post