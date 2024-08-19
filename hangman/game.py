import random
from .serializer  import StartGameSerializer
from  .model import GameRequest


letter_list = ['Hangman', 'Python', 'Audacix', 'Bottle', 'Pen']

#Start the Play Game
def initiate_game():
    picked_word = initiate_the_word()
    number_of_guess_allow = round(len(picked_word)/2)

   # gamerequest = GameRequest.objects.all()

    #gamerequest.__setattr__('gameid',1)
   # gamerequest.__setattr__('gamestate',2)
    #gamerequest.__setattr__('word',picked_word)
    #gamerequest.__setattr__('numberofattempts',number_of_guess_allow)

    #serializer = StartGameSerializer(gamerequest , many = True)

    return (picked_word,number_of_guess_allow)

#Initiate and Allocate the Game
def initiate_the_word():
    
    return random.choice(letter_list)



def play_game(guess, word,number_of_guess_allow):
   guessedLetter = []
   return_letter =""
   number_of_guess_allow -=1
   
   if(guess in word):
     guessedLetter.append(guess)  
    
   for letter in word:
        if letter in guessedLetter:
           print(f"{letter}",end="")
           return_letter(f"{letter}",end="")
        else:
           print(" _ ",end="")
           return_letter(" _ ",end="")



