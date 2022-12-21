from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Post, Comment
from blog.forms import CommentForm

# Create your views here.


# view to show list of all blogs
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


# view to show all blogs belongs which belongs to given category
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__category_name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


# view to show particular blog with all comments added to it
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                comment_author=form.cleaned_data["author"],
                comment_body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }

    return render(request, "blog_detail.html", context)


# view for deleting a comment
def blog_delete(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        comments.delete()
        return HttpResponseRedirect('/api/v1/blog/%d' % post.pk)
