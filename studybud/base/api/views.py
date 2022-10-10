from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)
    

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all() 
    return Response(rooms)
