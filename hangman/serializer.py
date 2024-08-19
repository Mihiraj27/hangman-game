from rest_framework import serializers
from .model import GameRequest
from .model import GameState


class GameRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRequest
        fields = '__all__'


class StartGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRequest
        fields = {'gameid','gamestate','word','numberofattempts'}


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameState
        fields = '__all__'