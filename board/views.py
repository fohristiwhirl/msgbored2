from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Message


@login_required
def msg_submit(request):

    if request.method != "POST":
        return redirect("/board/")

    di = request.POST

    try:
        s = di["message"]
    except KeyError:
        return redirect("/board/")
    if s == "":
        return redirect("/board/")

    q = Message(text = s)
    q.save()

    return redirect("/board/")


@login_required
def destroy_all(request):

    if request.method != "POST":
        return redirect("/board/")

    Message.objects.all().delete()
    return redirect("/board/")


@login_required
def index(request):

    username = None
    if request.user.is_authenticated():
        username = request.user.username

    context = {
        "msg_list": [msg for msg in Message.objects.all()],
        "username": username,
    }

    return render(request, "board/index.html", context)
