from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from .models import Room , Topic, Comment
from .forms import Comment
# Create your views here.


def index(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''
    room = Room.objects.filter(
        Q(topic__name__contains = q)|
        Q(title__contains = q)
    )
    topic = Topic.objects.all()
    context = {'room': room, 'topic': topic}

    return render(request, 'Blog\home.html',context)

def new(request , pk):
    new = Room.objects.get(id = pk)
    comment = Comment.objects.filter(room__id = pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('comment')
        comment = Comment.objects.create(room = new, name = name, description = description)
        comment.save()
        
        return redirect(request.path)

    context = {'new':new,'comment':comment,}
    return render(request, 'Blog/new.html',context)

