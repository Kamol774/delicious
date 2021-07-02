from django.shortcuts import redirect, render

from now.delicious.src.dashboard.follower.forms import FollowersForm
from now.delicious.src.front.models import Followers


def followers_create(request):
    model = Followers()
    form = FollowersForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("followers_list")
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'followers/form.html', ctx)


def followers_list(request):
    followerss = Followers.objects.all()
    ctx = {
        'followerss': followerss
    }
    return render(request, 'followers/list.html', ctx)


def followers_edit(request, pk):
    model = Followers.objects.get(pk=pk)
    form = FollowersForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("followers_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'followers/form.html', ctx)


def followers_delete(request, pk):
    model = Followers.objects.get(pk=pk)
    model.delete()
    return redirect("followers_list")