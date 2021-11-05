#This program was programmed by Simon Christianson
#It was made on 11/3/21
#This program allows the user to select a max value in which they would like to guess from.
#For example if they input 10 they would have to guess in between 1-10.  If they guess incorrectly the program will let them know if their guess is too high or low.
#Then it gives the option to run again after the user guesses the right number.

import random;
Run = True
Play = True
AskInput = True
while Play == True:
    while AskInput == True:
        MV = (input("What should the maximum number for this game be?(Must be an Integer)"))
        if MV.isnumeric():
            AskInput = False
    MV = int(MV)
    Number =random.randint(1,MV)
    Guess = int(input("\nGuess my Number: "))
    while Guess!= Number:
        if Guess <= Number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high")
        Guess = int(input("\nGuess my Number: "))

    print("You Guessed my number")
    Run = input("\nWould you lke to play again (Y or N)")
    if Run.lower() == "n":
        print("\nThank you for playing!")
        Play = False
        #print("\nThank you for playing!")






