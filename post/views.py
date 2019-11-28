from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from .models import Post
from .forms import PostForm


def all_posts(request):
    data = Post.objects.filter(active = True)
    Context={
        'all_posts':data,
    }
    return render(request, 'all_posts.html', Context)
    

def post(request, id):
    post_data = get_object_or_404(Post, id = id)
    Context = {
        'post_data': post_data,
    }
    return render(request, 'detail.html', Context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')
    else:
        form = PostForm()

    context = {
        'form' : form,
    }

    return render(request, 'create.html', context)

def edit_post(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)

    context = {
        'form' : form,
    }

    return render(request, 'edit.html', context)