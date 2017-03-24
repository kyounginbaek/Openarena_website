from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Page, ApprovedEmail
from .forms import PostForm, CommentForm, PageForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required()
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required()
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required()
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)


@login_required()
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if 'viewed' in request.session and request.session['viewed']:
        request.session['has_commented'] = False
    if 'has_commented' in request.session:
        request.session['viewed'] = True
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            request.session['has_commented'] = True
            request.session['viewed'] = False
            if request.user.is_authenticated():
                comment.approve()
            if len(ApprovedEmail.objects.filter(email_address=comment.email_address)) > 0:
                request.session['preapproved'] = True
                comment.approve()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html',
                  {'form': form, 'post': post})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    approved_email = ApprovedEmail(email_address = comment.email_address)
    comment.approve()
    approved_email.save()
    return redirect('blog:post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail', pk=post_pk)


def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'blog/page_detail.html', {'page': page})


@login_required()
def page_edit(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == "POST":
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            return redirect('blog:page_detail', pk=page.pk)
    else:
        form = PageForm(instance=page)
    return render(request, 'blog/page_edit.html', {'form': form})


@login_required()
def page_new(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save()
            return redirect('blog:page_detail', pk=page.pk)
    else:
        form = PageForm()
    return render(request, 'blog/page_edit.html', {'form': form})


@login_required()
def new_comments_list(request):
    comments = Comment.objects.filter(approved_comment=False).order_by('created_date')
    return render(request, 'blog/new_comments_list.html', {'comments': comments})


@login_required
def comment_approve_list(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    approved_email = ApprovedEmail(email_address = comment.email_address)
    comment.approve()
    approved_email.save()
    return redirect('blog:new_comments_list')


@login_required
def comment_remove_list(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:new_comments_list')


