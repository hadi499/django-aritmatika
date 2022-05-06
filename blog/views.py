from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts}

    return render(request, 'blog/index.html', context)


def create(request):
    post_form = PostForm(request.POST)

    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()

        return redirect('home')

    return render(request, 'blog/index.html')
