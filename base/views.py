from django.shortcuts import render
from .models import Room
 
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
    room= Room.objects.get(id=pk)
    context={'room':room}
    return render(request, 'base/room.html',context)