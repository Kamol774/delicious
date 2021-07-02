from django.shortcuts import render
from ..models import Blog


def blog_post(request):
    blog = Blog.objects.all()
    ctx = {
        "blogs": blog
    }
    return render(request, 'blog-post.html', ctx)
