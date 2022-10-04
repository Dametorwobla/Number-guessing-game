#Number guessing game 
#The computer picks a number between 1 and 100
#A player guesses it and the computer tells whether it's low or high

import random
print ("\tWelcome to 'Guess my number game'! ")
print ("\n I'm thinking of a number between 1 and 100")
print ("\n Try and guess it in few attempts as possible")

the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

#guess loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    tries += 1

print(("\n CONGRATULATIONS! You guessed right and the number was: ", the_number))
print("And it only took you ", tries, "tries! \n")

