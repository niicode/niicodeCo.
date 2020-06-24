from django.shortcuts import render, redirect 
from .models import Post 
from .forms import PostForm 
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'niicodeCo/index.html')

def blog(request):
	mydata = Post.objects.filter(is_published=True)
	post_form = PostForm()
	return render(request, 'niicodeCo/blog.html',{'content': mydata, 
		'post_form': post_form})

def admin(request):
	return HttpResponse("<h1>This page is on vacation</h1>")

@login_required
def unpublished_posts(request):
	mydata = Post.objects.filter(is_published=False)
	return render(request, 'niicodeCo/blog.html', {'content': mydata})


def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.published_date = datetime.now()
			post.save()
			return redirect('niicodeCo/blog.html')
		else:
			return render(request, 'niicodeCo/post_new.html', {'post_form': form})
	else:
		form = PostForm()
		return render(request, 'post_new.html', {'post_form': form})
