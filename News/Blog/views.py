from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Room , Topic

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
    context = {'new':new}
    return render(request, 'Blog/new.html',context)

