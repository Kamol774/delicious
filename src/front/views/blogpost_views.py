from django.shortcuts import render

def blog_post(request):
    return render(request, 'blog-post.html')