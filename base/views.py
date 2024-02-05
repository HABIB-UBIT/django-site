from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import *
from .forms import *
 
# Create your views here.
# rooms=[
#     {'id':1,'name':'Lets learn python'},
#     {'id':2,'name':'Lets learn rust'},
#     {'id':3,'name':'Lets learn Go'},
# ]

def loginpage(request):
    page= 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username= request.POST.get('username').lower()
        password= request.POST.get('password')
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,"User doesn't exist")
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "USername and Password doesn't exist")

    context={'page':page}
    return render(request, 'base/login_registeration.html', context)

def logoutuser(request):
    logout(request)
    return redirect('home')

def registeruser(request):
    form= UserCreationForm()
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)   #### commit = false holds the data for few moments so we can apply different changes. We want to give the access to the user right away 
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"An occured during registeration. Please try again")
    context={'form':form}
    return render(request, 'base/login_registeration.html', context)

def home(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    rooms= Room.objects.filter(
        Q(topic__name__icontains=q)  |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )    ### this is what we call query set  query_set= ModelName.objects.method()
    topics= Topics.objects.all()
    room_count= rooms.count()
    context= {'rooms':rooms, 'topics':topics, 'room_count': room_count}
    return render(request, 'base/home.html', context )

def room(request,pk):
    room= Room.objects.get(id=pk)
    room_messages= room.message_set.all()     ##### we are asking for all the messages of that specific room   ### We are intrested in getting all the messages of that specific room
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('room', pk=room.id)
    context={'room':room, 'room_messages':room_messages}
    return render(request, 'base/room.html',context)

######### CREATE FUNCTION ###########
@login_required(login_url='login')
def createroom(request):
    form= RoomForm()
    if request.method == 'POST':
        form= RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        
    context={'form':form}
    return render(request, 'base/room_form.html', context)

######### UPDATE FUNCTION ###########
@login_required(login_url='login')
def updateroom(request,pk):
    room= Room.objects.get(id=pk)
    form= RoomForm(instance = room)
    if request.user != room.host:
        return HttpResponse('You are not allowed to edit here')
    if request.method=='POST':
        form= RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect ('home')

    context={'form': form}
    return render (request, 'base/room_form.html', context)

######### DELETE FUNCTION ###########
@login_required(login_url='login')
def deleteroom(request,pk):
    room= Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed to edit here')
    if request.method=='POST':
        room.delete()
        return redirect ('home')
    return render(request, 'base/delete.html', {'obj': room})

