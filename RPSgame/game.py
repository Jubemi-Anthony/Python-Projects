import random
options = ["rock", "paper", "scissors"]
myScore = 0
computerScore = 0
gameOn = True

def announce(m,c):
    print(f"Your input: {m}, Computer input: {c}")

def announce2():
    print(f"Your Score: {myScore}, Computer Score: {computerScore}")

while gameOn:
    userInput = input("Enter 'rock', 'paper', 'scissors' or 'exit': ")
    userInput = userInput.lower()
    computerInput = random.choice(options)

    if userInput == 'exit':
        gameOn = False
        print("You Ended the Game")
        announce2()

    if userInput == 'rock':
        if computerInput == 'rock':
            announce(userInput,computerInput)
            print("The game is a draw")
            announce2()
        elif computerInput == 'paper':
            announce(userInput,computerInput)
            print("Computer won this round")
            computerScore += 1
            announce2()
        elif computerInput == 'scissors':
            announce(userInput,computerInput)
            print("You won this round")
            myScore += 1
            announce2()

    if userInput == 'paper':
        if computerInput == 'rock':
            announce(userInput,computerInput)
            print("You won this round")
            myScore += 1
            announce2()
        elif computerInput == 'paper':
            announce(userInput,computerInput)
            print("The game is a draw")
            announce2()
        elif computerInput == 'scissors':
            announce(userInput,computerInput)
            print("Computer won this round")
            computerScore += 1
            announce2()

    if userInput == 'scissors':
        if computerInput == 'rock':
            announce(userInput,computerInput)
            print("Computer won this round")
            computerScore += 1
            announce2()
        elif computerInput == 'paper':
            announce(userInput,computerInput)
            print("You won this round")
            myScore += 1
            announce2()
        elif computerInput == 'scissors':
            announce(userInput,computerInput)
            print("The game is a draw")
            announce2()