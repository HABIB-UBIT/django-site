from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/:id'
    ]
    # return JsonResponse(routes, safe=False)              ### Safe is allowing us to turn the list (routes) into a json list
    return Response(routes)

@api_view(['GET']) 
def getRooms(request):
    rooms= Room.objects.all()
    serializer= RoomSerializer(rooms, many=True)         ### many refers to how many objects you want to serialize, in our case we are serializing the queryset which is objects.all() (so many objects are there)
    return Response(serializer.data)

@api_view(['GET']) 
def getRoom(request, pk):
    room= Room.objects.get(id=pk)
    serializer= RoomSerializer(room, many=False)         ### many refers to how many objects you want to serialize, in our case we are serializing the queryset which is objects.get() (only a single objects)
    return Response(serializer.data)