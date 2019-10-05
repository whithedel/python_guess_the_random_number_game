from random import randint
randomNum = randint(1,100)

def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prGreen(skk):
    for x in skk:
        print("\033[92m {}\033[00m" .format(x))


msg= ["WELCOME TO GUESS ME!",
"I'm thinking of a number between 1 and 100",
"If your guess is more than 10 away from my number, I'll tell you you're COLD",
"If your guess is within 10 of my number, I'll tell you you're WARM",
"If your guess is farther than your most recent guess, I'll say you're getting COLDER",
"If your guess is closer than your most recent guess, I'll say you're getting WARMER",
"LET'S PLAY!"]
prGreen(msg)
guesses= [0]

while True:
   myGuess = int(input('\033[96m guess a random number between 1 to 100 \n\n\033[00m'))
   
   if myGuess < 1 or myGuess > 100:
       prRed('OUT OF BOUNDS')
       continue
   
   if myGuess == randomNum:
       prPurple(f'Excellent it only took you {len(guesses)} guesse(s)!!!')
       break

   guesses.append(myGuess)

   if len(guesses) >= 2:
       if abs(randomNum - myGuess) < abs(randomNum - guesses[-2]):
           prYellow('WARMER!!!')
       else:
           prRed('COLDER!!!')
   else:
       if abs(randomNum - myGuess) <= 10 :
           prRed('COlD!!!')
       else :
           prYellow('WARM!!!')