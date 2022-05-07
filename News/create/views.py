from pydoc_data.topics import topics
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout,decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from Blog.models import Room
from Blog.models import Topic as Topics

from .forms import RoomForm, TopicForm
from django.contrib.auth.models import Permission

# Create your views here.




class LoginView(View):
    def get(self,request):
        return render(request, 'create/index.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        authen = authenticate(username = username, password = password)
        if authen: 
            login(request,authen)
            return redirect('push')
        return HttpResponse('tai khoan khong ton tai')

class index(LoginRequiredMixin,View):
    login_url= 'login'
    def get(self,request):
        return HttpResponse('hello')


@decorators.login_required(login_url='login')
def Push(request):
    room = Room.objects.all()
    return render(request,'create/push.html',{'room':room})

@decorators.login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('home')

@decorators.login_required(login_url='login')
def create (request):
    if request.user.has_perm('create.add_create'):
        form = RoomForm()
        
        if request.method == 'POST':
            form = RoomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('push')
        context = {'form': form}
        return render(request, 'create/createpage.html',context)
    else: return HttpResponse('ban khong co quyen')

@decorators.login_required(login_url='login')
def update(request,pk):
    if request.user.has_perm('create.change_update'):
        room = Room.objects.get(id= pk)
        form = RoomForm(instance = room)
        if request.method == 'POST':
            form = RoomForm(request.POST, instance = room)
            if form.is_valid():
                form.save()
                return redirect('push')

        context = {'form': form }

        return render(request,'create/createpage.html',context)
    else: return HttpResponse('ban khong co quyen')

@decorators.login_required(login_url='login')
def delete(request,pk):
    if request.user.has_perm('create.delete_delete'):
        room = Room.objects.get(id=pk)
        room.delete()
        return redirect('push')
    else : return HttpResponse('ban khong co quyen')

@decorators.login_required(login_url='login')
def Topic(request):
    if request.user.has_perm('create.topic'):
        topics = Topics.objects.all()

        context = {'topic': topics}
        return render(request, 'create/hometopic.html',context)
    else : return HttpResponse('ban khong cos quyen')

@decorators.login_required(login_url='login')
def AddTopic(request):
    if request.user.has_perm('create.add_create'):
        form = TopicForm()
        
        if request.method == 'POST':
            form = TopicForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('topic')
        context = {'form': form}
        return render(request, 'create/topic.html',context)
    else: return HttpResponse('ban khong co quyen')

@decorators.login_required(login_url='login')
def updatetopic(request,pk):
    if request.user.has_perm('create.change_update'):
        topic = Topics.objects.get(id= pk)
        form = TopicForm(instance = topic)
        if request.method == 'POST':
            form = TopicForm(request.POST, instance = topic)
            if form.is_valid():
                form.save()
                return redirect('topic')

        context = {'form': form }

        return render(request,'create/topic.html',context)
    else: return HttpResponse('ban khong co quyen')

@decorators.login_required(login_url='login')
def deletetopic(request,pk):
    if request.user.has_perm('create.delete_delete'):
        topic = Topics.objects.get(id=pk)
        topic.delete()
        return redirect('topic')
    else : return HttpResponse('ban khong co quyen')

