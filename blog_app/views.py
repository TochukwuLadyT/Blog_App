from django.shortcuts import render, redirect
from .forms import *


def home(request):
    post = Post.objects.all()
    context = {
        "post": post
    }
    return render(request, "blog_list.html", context)


def add_post(request):
    form = AddPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        "form": form
    }

    return render(request, "add_post.html", context)


def update_blog(request, pk):
    post = Post.objects.get(id=pk)
    form = UpdatePostForm(instance=post)
    if request.method == "POST":
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        "form": form
    }
    return render(request, 'update_blog.html', context)


def delete_post(pk):
    Post.objects.get(id=pk).delete()
    return redirect('home')
