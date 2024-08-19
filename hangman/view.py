from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .model import GameRequest
from .serializer import GameRequestSerializer
from .serializer import StartGameSerializer
from .game import *

@api_view(['POST'])
def start_new_game():
    return Response(start_new_game())

@api_view(['POST'])
def game_state(request,id):
    try:
       gamerequest = GameRequest.objects.get(pk=id)
       serializer = GameRequestSerializer(gamerequest, data = request.data)
       if serializer.is_valid():
        date = play_game(serializer.game_guess,serializer.initiate_the_word,serializer.numberofattempts)
        serializer = GameRequestSerializer(data=date)
        serializer.save()
        return Response(serializer.data , status = status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def game_guess(request,id):
    try:
       gamerequest = GameRequest.objects.get(pk=id)
       serializer = GameRequestSerializer(gamerequest, data = request.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
