from random import randint
import sys 
from termcolor import colored, cprint 

randomNum = randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses= [0]

while True:
   myGuess = int(input('guess a random number between 1 to 100 \n\n'))
   
   if myGuess < 1 or myGuess > 100:
       print('OUT OF BOUNDS')
       continue
   
   if myGuess == randomNum:
       print(f'Excellent it only took you {len(guesses)} guesse(s)!!!')
       break

   guesses.append(myGuess)

   if len(guesses) >= 2:
       if abs(randomNum - myGuess) < abs(randomNum - guesses[-2]):
           print('WARMER!!!')
       else:
           print('COLDER!!!')
   else:
       if abs(randomNum - myGuess) <= 10 :
           print('COlD!!!')
       else :
           print('WARM!!!')