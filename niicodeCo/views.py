from django.shortcuts import render, redirect
from .models import Post, PostComment
from .forms import PostForm, PostCommentForm
from datetime import datetime
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'niicodeCo/index.html')


def blog(request):
    posts = Post.objects.all()
    return render(request, 'niicodeCo/blog.html', {'mycontent': posts})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.now()
            post.save()
            return redirect('/')
        else:
            return render(request, 'niicodeCo/post_new.html', {'post_form': form})
    else:
        form = PostForm()
        return render(request, 'niicodeCo/post_new.html', {'post_form': form})


def post_detail(request, article_id):
    post = Post.objects.get(id=article_id)
    return render(request, 'niicodeCo/post_details.html', {'myarticle': post})

@login_required()
def unpublished_posts(request):
    mydata = Post.objects.filter(is_published=False)
    return render(request, 'niicodeCo/blog', {'mycontent': mydata})

@login_required()
def post_new_comment(request):
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        article_id = request.POST.get('article_id')
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.objects.get(id=int(article_id))
            comment.save()
            return redirect('/gideon/')
        else:
            return render(request, 'niicodeCo/post_new_comment.html', {'comment_form': form})


def post_new_comment_form(request):
    article_id = request.POST.get('article_id')
    form = PostCommentForm()
    return render(request, 'niicodeCo/post_new_comment.html', {"article_id": article_id, 'comment_form': form})




def edit_post(request, article_id):
    my_post = Post.objects.get(id=article_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=my_post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modified_date = datetime.now()
            post.save()
            return redirect('/niicode/blog/')
        else:
            return render(request, 'niicodeCo/post_edit.html', {'post_form': form})
    else:
        form = PostForm(instance=my_post)
        return render(request, 'niicodeCo/post_edit.html', {'post_form': form, 'article_id': article_id})


def post_detail(request, article_id):
    mydata = Post.objects.get(id=article_id)
    comments = PostComment.objects.filter(post=mydata)[:1]
    return render(request, 'niicodeCo/post_detail.html', {'myarticle': mydata, "article_id": article_id, "comments":comments})


def delete_post(request, article_id):
    mydata = Post.objects.get(id=article_id)
    mydata.delete()
    return redirect('/niicode/blog/')


def publish_post(request, article_id):
    if request.method == 'POST':
        mydata = Post.objects.get(id=article_id)
        mydata.is_published = True
        mydata.save()

        return redirect('/niicode/blog/')
    else:
        return redirect('/niicode/blog/')


def unpublish_post(request, article_id):
    if request.method == 'POST':
        mydata = Post.objects.get(id=article_id)
        mydata.is_published = False
        mydata.save()

        return redirect('/niicode/blog/')
    else:
        return redirect('/niicode/blog/')

