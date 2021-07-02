from django.shortcuts import render

def recipes_post(request):
    return render(request, 'receipe-post.html')