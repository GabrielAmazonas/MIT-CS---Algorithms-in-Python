# Binary Search
max = 100
min = 0
guess = max / 2
found = False


print("Please think of a number between 0 and 100!")
while (found == False):
    guess =  (max + min) // 2
    print("Is your secret number " + str(guess) + "?")
    userInput = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if (userInput == "c" ):
        found = True
        print("Game over. Your secret number was: " + str(guess))
        break
    elif (userInput == "h"):
        max = guess
    elif (userInput == "l"):
        min = guess
    else:
         print("Sorry, I did not understand your input.")
        
     

