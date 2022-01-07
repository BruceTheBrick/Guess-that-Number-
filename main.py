from Randy import Randy


def main():
    randy = Randy(1, 10)
    menu(randy)
    


   

def run(randy):
    userInput = ""
    while userInput != "exit":
        randy.sayHello()
        userInput = input()

        if(isInt(userInput)):
            if(randy.checkGuess(int(userInput))):
                print("You got it!")
            else:
                print("Better luck next time!")
        else:
            print("Not an int!")

        randy.genNumber()
    print("It was nice playing with you!")

def settings(randy):
    upper = 0
    lower = 0
    print("Please enter the lower bound for random numbers")
    dashedLine()
    lower = input()
    while(not isInt(lower)):
        invalidInput()
        lower = input()

    print("Please enter the upper bound for random numbers")
    dashedLine()
    upper = input()
    while(not isInt(upper) or int(upper) <= int(lower)):
        invalidInput(2)
        upper = input()

    

    randy.setUpper(int(upper))
    randy.setLower(int(lower))
    randy.genNumber()
    menu(randy)

def close(randy):
    print("Thanks for playing!")
    return

def menu(randy):
    userInput = ""
    switch_case = {
        1 : run,
        2 : settings,
        3 : close
    } 
    print("Welcome to Randy the Random Number Guesser!")
    dashedLine()
    print("Please select an option:")
    print("1. Play!")
    print("2. Settings")
    print("3. Exit")
    dashedLine()
    while(not isInt(userInput)):
        userInput = input()
        if(isInt(userInput)):
            switch_case[int(userInput)](randy)
        else:
            print("That's not a number. Try again.")



def dashedLine():
    print("-------------------------------------------")

def invalidInput(error = 1):
    if(error == 1):
        print("Please select enter a valid number")
    else:
        print("Please select an upper bound that is greater than the lower bound")

def isInt(var):
    temp = 0
    try:
        temp = int(var)
        return True
    except:
        return False

if __name__ == "__main__":
    main()