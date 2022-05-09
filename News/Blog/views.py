from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from .models import Room , Topic, Comment
from .forms import Comment
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''
    room = Room.objects.filter(
        Q(topic__name__contains = q)|
        Q(title__contains = q)
    )
    topic = Topic.objects.all()
    paginator = Paginator(room, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'room': room, 'topic': topic,'page_obj': page_obj}

    return render(request, 'Blog\index1.html',context)

def new(request , pk):
    new = Room.objects.get(id = pk)
    comment = Comment.objects.filter(room__id = pk)
    topic = Topic.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('comment')
        if request.POST.get('comment') =='':
            return redirect(request.path)
        if name.strip() == '':
            name = "Guest"
        comment = Comment.objects.create(room = new, name = name, description = description)
        comment.save()
        
        return redirect(request.path)

    context = {'new':new,'comment':comment,'topic':topic}
    return render(request, 'Blog/single-blog.html',context)

