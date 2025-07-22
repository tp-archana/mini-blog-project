from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .models import *
from .forms import *


# Create your views here.

def post_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_view')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def post_view(request):
    posts = PostModel.objects.all()
    return render(request, 'list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    comment = post.comments.all()
    if request.method == 'POST':
        form = blogForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)

    else:
        form = blogForm()
    return render(request, 'detail.html', {'post': post, 'comments': comment, 'form': form})
