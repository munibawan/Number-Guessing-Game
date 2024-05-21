import random

#First input from user
top_of_range = input("Type a number ")
print("The number to be guessed will be with-in numbers 0 to " + top_of_range)

#print(rand)
convert_top_of_range = int(top_of_range)
rand = random.randint(0, convert_top_of_range)

#Guesses
guesses = 0
while True:
    guesses += 1
    guessed = input("Guess the number: ")
    c_guessed = int(guessed)
    if c_guessed == rand:
        print("You got it!")
        break
    else:
        if c_guessed < rand:
            print("Your guess is below the number")
        else:
            print("Your guess is above the number")
             
print("You got it in", guesses, "guesses")    

#The program have ended