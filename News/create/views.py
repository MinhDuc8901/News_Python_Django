from pydoc_data.topics import topics
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout,decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from Blog.models import Room
from Blog.models import Topic as Topics
from django.core.paginator import Paginator
from .forms import RoomForm, TopicForm
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User 

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
        return render (request,'create/index1.html')


@decorators.login_required(login_url='login')
def Push(request):
    room = Room.objects.all()
    paginator = Paginator(room, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'create/index2.html',{'room':room, 'page_obj': page_obj})

@decorators.login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('home')

@decorators.login_required(login_url='login')
def create (request):
    if request.user.has_perm('create.add_create'):
        form = RoomForm()
        
        if request.method == 'POST':
            form = RoomForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('push')
        context = {'form': form}
        return render(request, 'create/index5.html',context)
    else: return HttpResponse('ban khong co quyen')

@decorators.login_required(login_url='login')
def update(request,pk):
    if request.user.has_perm('create.change_update'):
        room = Room.objects.get(id= pk)
        form = RoomForm(instance = room)
        if request.method == 'POST':
            form = RoomForm(request.POST,request.FILES, instance = room)
            if form.is_valid():
                form.save()
                return redirect('push')

        context = {'form': form }

        return render(request,'create/index5.html',context)
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
        paginator = Paginator(topics, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'topic': topics,'page_obj': page_obj}
        return render(request, 'create/index3.html',context)
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
        return render(request, 'create/index4.html',context)
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

        return render(request,'create/index4.html',context)
    else: return HttpResponse('ban khong co quyen')

@decorators.login_required(login_url='login')
def deletetopic(request,pk):
    if request.user.has_perm('create.delete_delete'):
        topic = Topics.objects.get(id=pk)
        topic.delete()
        return redirect('topic')
    else : return HttpResponse('ban khong co quyen')




