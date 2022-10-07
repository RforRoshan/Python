import random
class guess_no:
    def __init__(self,name):
        self.name=name
        self.no=random.randint(1,100)
        print(self.no)
    def start(self):
        a=0
        self.i=0
        print("Player "+self.name)
        print("-"*20)
        print("Pick a number between 1 to 100\nYou have 10 trials to guess that")
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

p1=guess_no("Ram")
p2=guess_no("Syam")
p1.start()
p2.start()
p1.showresult()
p2.showresult()