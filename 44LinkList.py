class node:                      #New node body
    def __init__(self,data):
        self.data=data
        self.next=None


class linklist:                  
    def __init__(self):
        self.head=None           #Head pointer

#Insert node at begening
    def beginsert(self,data):   
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        
#Insert node at End
    def endinsert(self,data):  
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            return
        current=self.head
        while(current.next!=None):
            current=current.next
        current.next=new_node

#Insert node at perticular position
    def posinsert(self,ind,data):      
        if ind==0:      #Insert node at begening
            new_node=node(data)
            new_node.next=self.head
            self.head=new_node
            return
        new_node=node(data)
        current=self.head
        if ind==size+1:  #Insert node at End
            while(current.next!=None):
                current=current.next
            current.next=new_node
            return
            
        cuind=1
        while(cuind!=ind):
            current=current.next
            cuind+=1
        new_node.next=current.next
        current.next=new_node

#Delete first node
    def firstdelete(self):
        current=self.head
        self.head=current.next
        return current.data

#Delete node by giving data. It return true if data found and deleted
    def delnode(self,data):          
        if self.head.data==data:
            self.head=self.head.next
            return True
        current=self.head
        while(current.next):
            if current.next.data==data:
                current.next=current.next.next
                return True
            current=current.next
        return False
                
#Delete last node
    def lastdelete(self):       
        if self.head.next==None:
            self.head=None
            return
        current=self.head
        while(current.next.next):
            current=current.next
        current.next=None

#Return node index of given data
    def search(self,data):  
        ind=0
        current=self.head         
        while(current):
            if current.data==data:
                return ind
            ind+=1
            current=current.next
        return -1

# Display linklist
    def display(self):           
        if self.head==None:
            print("Link List is Empty")
        else:
            current=self.head
            while(current):
                print(current.data,end="    ")
                current=current.next
            print()

#Return total no. of Node
    def countnode(self):        
        ind=0
        current=self.head
        while(current):
            ind+=1
            current=current.next
        return ind

#Reverse link list
    def revlinklist(self):
        if self.head.next==None:
            return
        current=self.head
        nex=current.next
        current.next=None
        while(nex):
            pre=current
            current=nex
            nex=nex.next
            current.next=pre
        self.head=current

#swap the node in link list
    def swap(self,a,b):
        if a==0 and b==1:           #if node 1st and node 2
            current=self.head
            self.head=current.next
            pre=self.head.next
            self.head.next=current
            current.next=pre
            return
        if abs(a-b)==1:             #if adjacent node
            ind=0
            current=self.head
            c=b
            if a>b:
                c=a
            while(ind!=c-2):                   
                current=current.next           
                ind+=1                          
            ne=current.next
            pre=ne.next
            current.next=pre
            ne.next=pre.next
            pre.next=ne
            return
        if a==0 or b==0:
            ind=0
            c=a
            if a==0:
                c=b
            current1=self.head
            pre2=current1
            nex1=current1.next
            while(ind!=c-1):
                ind+=1
                pre2=pre2.next
            current2=pre2.next
            nex2=current2.next
            #swap
            self.head=current2
            current2.next=nex1
            pre2.next=current1
            current1.next=nex2
            return
        ind=0
        c=a
        if a<b:
            c=b         #  c will have big value and d will have small value
        d=a+b-c
        current=self.head
        pre1=current
        pre2=current
        while(ind!=c-1):
            ind+=1
            if ind<=d-1:
                pre1=pre1.next
            pre2=pre2.next
        current1=pre1.next
        current2=pre2.next
        nex1=current1.next
        nex2=current2.next
        #swap
        pre1.next=current2
        current2.next=nex1
        pre2.next=current1
        current1.next=nex2
            
# Return single node
    def singlenode(self,ind):  
        current=self.head     
        temp=0    
        while(temp!=ind):
            temp+=1
            current=current.next
        return current.data


if __name__=="__main__":
    s=linklist()
    ch=True
    while(ch):
        print("*"*43)
        print("CHOICE  LINK LIST OPERATION")
        print("  1     Insert N node")
        print("  2     Insert node at begning")
        print("  3     Insert node at perticular position")
        print("  4     Insert node at end")
        print("  5     Delete first node")
        print("  6     Delete last node")
        print("  7     Delete node")
        print("  8     Display link list")
        print("  9     Display single node")
        print("  10    Search a node")
        print("  11    Count number of node")
        print("  12    Reverse link list")
        print("  13    Swap node")
        print("  14    Bubble sort")
        print("  15    Exit")
        print("*"*43)
        a=input("Enter your choice= ")

        if a=='1':
            n=int(input("Enter number of node you want to insert ="))
            for i in range(n):
                data=int(input("Enter data of node ="))
                s.endinsert(data)
            print(str(n)+" Node created")
            input("Press ENTER key to continue ")

        elif a=='2':
            data=int(input("Enter data of node ="))
            s.beginsert(data)
            print(str(data)+" inserted")
            input("Press ENTER key to continue ")

        elif a=="3":
            size=s.countnode()
            ind=int(input("Enter the index of node= "))
            if ind>=size or ind<0:
                print("Invalid index")
            else:
                data=int(input("Enter data of node= "))
                s.posinsert(ind,data)
                print(str(data)+" inserted")
            input("Press ENTER key to continue ")

        elif a=='4':
            data=int(input("Enter data of node ="))
            s.endinsert(data)
            print(str(data)+" inserted")
            input("Press ENTER key to continue ")

        elif a=='5':
            if s.countnode==0:
                print("Link List is Empty")
            else:
                print("Deleted Node is",s.firstdelete())
            input("Press ENTER key to continue ")

        elif a=='6':
            if s.countnode==0:
                print("Link List is Empty")
            else:
                s.lastdelete()
                print("Last node deleted")
            input("Press ENTER key to continue ")

        elif a=='7':
            if s.countnode==0:
                print("Link List is Empty")
            else:
                data=int(input("Enter data of node to delete ="))
                res=s.delnode(data)
                if res==False:
                    print("Node not found")
                else:
                    print("Node deleted")
            input("Press ENTER key to continue ")

        elif a=='8':
            s.display()
            input("Press ENTER key to continue ")

        elif a=='9':
            ind=int(input("Enter index of node= "))
            if ind>=s.countnode():
                print("Invalid index")
            else:
                print("Data at index",ind,"=",s.singlenode(ind))
            input("Press ENTER key to continue ")

        elif a=='10':
            if s.countnode==0:
                print("Link List is Empty")
            else:
                data=input("Enter data of node to search =")
                res=s.search(data)
                if res==-1:
                    print("Node not found")
                else:
                    print("Node found at index",res)
            input("Press ENTER key to continue ")

        elif a=='11':
            print("Total number of node=",s.countnode())
            input("Press ENTER key to continue ")

        elif a=='12':
            if s.countnode==0:
                print("Link list is empty")
            else:
                s.revlinklist()
            input("Press ENTER key to continue ")

        elif a=='13':
            a=int(input("Enter 1st node number= "))
            b=int(input("Enter 2nd node number= "))
            size=s.countnode()
            if a>size-1 or b>size-1 or a<0 or b<0:
                print("Invalid node position")
            else:
                s.swap(a,b)
            input("Press ENTER key to continue ")

        elif a=='14':
            size=s.countnode()
            for i in range(size):
                for j in range(size-i-1):
                    if s.singlenode(j)>s.singlenode(j+1):
                        s.swap(j,j+1)
            print("Link list sorted")
            input("Press ENTER key to continue ")

        elif a=='15':
            print("*"*43)
            print(' '*16+"THANK YOU")
            print("*"*43)
            ch=False
            
        else:
            print("Invalid input")
            input("Press ENTER key to continue ")