from delicious.src.dashboard.blog.form import BlogForm
from delicious.src.front.models import Blog
from django.shortcuts import render, redirect


class BlogViews:
    def list(self, request):
        blog = Blog.objects.all()
        ctx = {
            "blogs": blog
        }
        return render(request, "blog/list.html", ctx)

    def blog_create(self, request):
        model = Blog()
        form = BlogForm(request.POST or None, instance=model)
        if request.POST:
            form.is_valid()
            form.save()
            return redirect("blog_list")
        ctx = {
            "model": model,
            "form": form
        }
        return render(self, "blog/form.html", ctx)

    def blog_edit(self, request, pk):
        model = Blog.objects.get(pk=pk)
        form = BlogForm(request.POST or None, instance=model)
        if self.POST:
            form.is_valid()
            form.save()
            return redirect("blog_list")
        ctx = {
            "model": model,
            "form": form
        }
        return render(self, "blog/form.html", ctx)

    def blog_delete(self, request, pk):
        model = Blog.objects.get(pk=pk)
        model.delete()
        return redirect("blog_list")
