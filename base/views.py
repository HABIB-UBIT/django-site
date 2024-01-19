from django.shortcuts import render, redirect
from .models import Room
from .forms import *
 
# Create your views here.
# rooms=[
#     {'id':1,'name':'Lets learn python'},
#     {'id':2,'name':'Lets learn rust'},
#     {'id':3,'name':'Lets learn Go'},

# ]
def home(request):
    rooms= Room.objects.all()    ### this is what we call query set  query_set= ModelName.objects.method()
    context= {'rooms':rooms}
    return render(request, 'base/home.html', context )

def room(request,pk):
    # room= Room.objects.get(id=pk)
    room= Room.objects.get(id=pk)
    context={'room':room}
    return render(request, 'base/room.html',context)

######### CREATE FUNCTION ###########
def createroom(request):
    form= RoomForm()
    if request.method == 'POST':
        form= RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        
    context={'form':form}
    return render(request, 'base/room_form.html', context)

######### Update FUNCTION ###########
def updateroom(request,pk):
    room= Room.objects.get(id=pk)
    form= RoomForm(instance = room)
    if request.method=='POST':
        form= RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect ('home')

    context={'form': form}
    return render (request, 'base/room_form.html', context)


def deleteroom(request,pk):
    room= Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect ('home')
    return render(request, 'base/delete.html', {'obj': room})

