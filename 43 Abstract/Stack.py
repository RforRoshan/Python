class Stack:
    def __init__(self,size=100):
        self._maxsize = size
        self._size = 0
        self._stack = []

    def Push(self, data):
        if(self._size <= self._maxsize):
            self._stack.append(data)
            self._size += 1
        else:
            print("Stack is Full")

    def Pop(self):
        if(self._size > -1):
            self._size -= 1
            return self._stack.pop()
        else:
            return -1
    def peek(self):
        return self._stack[-1]

    def getsize(self):
        return self._size

    def printstack(self):
        for i in self._stack:
            print(i,end="   ")
        print()


if __name__=='__main__':
    s = Stack()
    ch=True
    while(ch):
        print("*"*43)
        print("CHOICE  STACK OPERATION")
        print("  1     Push an element")
        print("  2     Pop an element")
        print("  3     Show Last element")
        print("  4     Count total number of element")
        print("  5     Show stack")
        print("  6     Exit")
        print("*"*43)
        a=input("Enter your choice= ")
        if a=='1':
                data=int(input("Enter element to push ="))
                s.Push(data)
        elif a=='2':
            gg=s.Pop()
            if gg==-1:
                print("Stack is empty")
            else:
                print("Pop element =",gg)
            input("Press ENTER key to continue ")
        elif a=='3':
            print("The last element =",s.peek())
            input("Press ENTER key to continue ")
        elif a=='4':
            print("Total number of element =",s.getsize())
            input("Press ENTER key to continue ")
        elif a=='5':
            if s.getsize==0:
                print("Stack is Empty")
            else:
                print("Stack")
                s.printstack()
            input("Press ENTER key to continue ")
        elif a=='6':
                print("*"*43)
                print(' '*16+"THANK YOU")
                print("*"*43)
                ch=False
        else:
            print("Invalid input")
            input("Press ENTER key to continue ")