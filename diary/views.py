from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone


# Create your views here.

def post_list(request, pagenum = 1):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'diary/post_list.html', {'posts': posts})

def post_view(request, pk):
    post = Post.objects.get_object_or_404(pk=pk)
    
    return render(request, 'diary/post_view.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('diary.views.post_view', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'diary/post_edit.html', {'form':form})

def join(request):
    if request.method == "POST"
    