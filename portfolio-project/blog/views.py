from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def allblogs(request):
    posts = Post.objects
    return render(request, 'blog/allblogs.djt', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.djt', {'post': post})
