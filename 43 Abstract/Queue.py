class Queue:
    def __init__(self,size=100):
        self._maxsize = size
        self._size = 0
        self._queue = []

    def Enqueue(self, data):
        if(self._size <= self._maxsize):
            self._queue.append(data)
            self._size += 1
        else:
            print("Queue is Full")

    def Dequeue(self):
        if(self._size > -1):
            self._size -= 1
            return self._queue.pop(0)
        else:
            return -1
    def peek(self):
        return self._queue[0]

    def getsize(self):
        return self._size

    def printqueue(self):
        for i in self._queue:
            print(i,end=" ")
        print()


if __name__=='__main__':
    s = Queue(5)
    ch=True
    while(ch):
        print("*"*43)
        print("CHOICE  QUEUE OPERATION")
        print("  1     Enqueue")
        print("  2     Dequeue")
        print("  3     Peek")
        print("  4     Count total number of element")
        print("  5     Show queue")
        print("  6     Exit")
        print("*"*43)
        a=input("Enter your choice= ")
        if a=='1':
                data=int(input("Enter data ="))
                s.Enqueue(data)
        elif a=='2':
            gg=s.Dequeue()
            if gg==-1:
                print("Queue is empty")
            else:
                print("Dequeue element =",gg)
            input("Press ENTER key to continue ")
        elif a=='3':
            print("The first element =",s.peek())
            input("Press ENTER key to continue ")
        elif a=='4':
            print("Total number of element =",s.getsize())
            input("Press ENTER key to continue ")
        elif a=='5':
            if s.getsize==0:
                print("Queue is Empty")
            else:
                print("Queue")
                s.printqueue()
            input("Press ENTER key to continue ")
        elif a=='6':
                print("*"*43)
                print(' '*16+"THANK YOU")
                print("*"*43)
                ch=False
        else:
            print("Invalid input")
            input("Press ENTER key to continue ")