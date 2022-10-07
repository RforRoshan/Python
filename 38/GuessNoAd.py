import random
from tkinter import CENTER
from turtle import clearscreen
class guess_no:
    def __init__(self,name):
        self.name=name
        self.no=random.randint(1,100)
        print(self.no)
    def start(self):
        a=0
        self.i=0
        print("Player= "+self.name)
        print("Pick a number between 1 to 100\nYou have 10 trials to guess that")
        print()
        print("-"*20)
        while(a!=self.no and self.i<11):
            print("? ",end="")
            a=int(input())
            self.i+=1
            if a!=self.no:
                if a<self.no:
                    print("Not Correct, guess higher")
                else:
                    print("Not Correct, guess lower")
            else:
                print("Congratulations!!")
        if self.i==11:
            print("Game Over")
            print("Number= "+str(self.no))
        print("-"*20)
    def showresult(self):
        print("Name- "+self.name)
        print("Score = ",10-self.i+1)
        print("Excellent playing!")
        print("-"*20)
print("-"*20)
print(("Guess a Number Game"))
print("-"*20)
f=int(input("Enter number of players=  "))
print("-"*20)
for j in range(f):
    name=input("Enter name: ")
    print("-"*20)
    d=guess_no(name)
    d.start()
for j in range(f):
    d.showresult()
