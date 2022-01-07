import random

class Randy:
    num = 0
    lowerBound = 0
    upperBound = 0

    def __init__(self, lowerBound, upperBound):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.genNumber()

    def sayHello(self):
        print("Hi, I'm randy! Can you guess what number I'm thinking of?")

    def setUpper(self, upper):
        self.upperBound = upper
        
    def setLower(self, lower):
        self.lowerBound = lower

    def genNumber(self):
        self.num = random.randint(self.lowerBound, self.upperBound)
        return self.num

    def checkGuess(self, guess):
        return self.num == guess

    def getNum(self):
        return self.num
    
