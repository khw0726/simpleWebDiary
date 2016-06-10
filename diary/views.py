from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, JoinForm, LoginForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

def post_list(request, pagenum = 1):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'diary/post_list.html', {'posts': posts})

def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'diary/post_view.html', {'post':post})
def join(request):
    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary.views.post_list')
    else:
        form = JoinForm()
        
    return render(request, 'diary/join.html', {'form':form})

'''def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        print username, password
        
        user = authenticate(username = username, password = password)
        
        if user != None:
            #if user.is_active:
            login(request, user)
            return redirect('diary.views.post_view', pk = post.pk)
            #else:
            #    pass 
        else:
            messages.error(request, 'invalid user')
            form = LoginForm()
            return render(request, 'diary/login.html', {'form':form})
    else:
        form = LoginForm()
        return render(request, 'diary/login.html', {'form':form})'''
    

@login_required
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

