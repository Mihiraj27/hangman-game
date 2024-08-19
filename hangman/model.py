from django.db import models


#Create a Game Request Model

class GameRequest(models.Model):
    gameid = models.IntegerField()
    gamestate = models.IntegerField()
    letter = models.CharField(max_length=5)
    word = models.CharField(max_length=20)
    numberofattempts = models.ImageField()



    def __str__(self):
        return self.gameid +' ' +self.gamestate + ' ' +self.letter+ ' ' +self.word+' ' +self.numberofattempts 
    




class GameState(models.Model):
    stateid = models.IntegerField()
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.stateid +' ' +self.state


