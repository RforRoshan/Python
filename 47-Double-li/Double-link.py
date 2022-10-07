class node:                      #New node body
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class DoublyLinkedList:                  
    def __init__(self):
        self.head=None           #Head pointer
        self.tail=None

#Insert node at begening
    def beginsert(self,data):  
        #if head is none 
        if self.head==None:
            new_node=node(data)
            new_node.next=self.head
            self.head=new_node
            self.tail=new_node
        else:
            new_node=node(data)
            new_node.next=self.head
            new_node.prev=self.head
            self.head=new_node
            
#Insert node at End
    def endinsert(self,data):  
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
            return
        current=self.head
        while(current.next!=None):
            current=current.next
        current.next=new_node
        new_node.prev=current
        self.tail=new_node

#Insert node at perticular position
    def posinsert(self,ind,data,size):      
        if ind==0:      #Insert node at begening
            if self.head==None:
                new_node=node(data)
                new_node.next=self.head
                self.head=new_node
                self.tail=new_node
            else:
                new_node=node(data)
                new_node.next=self.head
                self.head.prev=new_node
                new_node.prev=None
                self.head=new_node

            return
        if ind==size:  #Insert node at End
            new_node=node(data)
            if self.head==None:
                self.head=new_node
                self.tail=new_node
                return
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=new_node
            new_node.prev=current
            self.tail=new_node
            return
            
        cuind=1
        current=self.head
        new_node=node(data)
        while(cuind!=ind):
            current=current.next
            cuind+=1
        new_node.next=current.next
        new_node.prev=current
        current.next.prev=new_node
        current.next=new_node
        

#Delete first node
    def firstdelete(self):
        current=self.head
        self.head=current.next
        if self.head!=None:
            self.head.prev=None
        return current.data

#Delete node by giving data. It return true if data found and deleted
    def delnode(self,data):          
        if self.head.data==data:
            self.head=self.head.next
            self.head.prev=None
            return True
        if self.tail.data==data:
            self.tail=self.tail.prev
            self.tail.next=None
            return True

        current=self.head
        while(current.next):
            if current.next.data==data:
                current.next=current.next.next
                current.next.prev=current
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
        self.tail=current

#Return node index of given data
    def Search(self,data):  
        ind=0
        current=self.head         
        while(current):
            if current.data==data:
                return ind
            ind+=1
            current=current.next
            
        return -1

# Display linklist from left to right
    def displayf(self):           
        if self.head==None:
            print("Link List is Empty")
        else:
            current=self.head
            while(current):
                print(current.data,end="    ")
                current=current.next
            print()

# Display linklist from right to left
    def displayb(self):           
        if self.head==None:
            print("Link List is Empty")
        else:
            current=self.tail
            while(current):
                print(current.data,end="    ")
                current=current.prev
            print()

#Return total no. of Node
    def countnode(self):        
        ind=0
        current=self.head
        while(current):
            ind+=1
            current=current.next
        return ind
   
# Return single node data
    def singlenode(self,ind):  
        current=self.head     
        temp=0    
        while(temp!=ind):
            temp+=1
            current=current.next
        return current.data


if __name__=="__main__":
    s=DoublyLinkedList()
    ch=True
    while(ch):
        print("*"*43)
        print("CHOICE  DOUBLY LINK LIST OPERATION")
        print("  1     Insert N node")
        print("  2     Insert node at begning")
        print("  3     Insert node at perticular index")
        print("  4     Insert node at end")
        print("  5     Delete first node")
        print("  6     Delete last node")
        print("  7     Delete node")
        print("  8     Display doubly link list from left to right")
        print("  9     Display doubly link list from right to left")
        print("  10    Display single node")
        print("  11    Search a node")
        print("  12    Count number of node")
        print("  13    Exit")
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
            if ind>size or ind<0:
                print("Invalid index")
            else:
                data=int(input("Enter data of node= "))
                s.posinsert(ind,data,s.countnode())
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
            s.displayf()
            input("Press ENTER key to continue ")
        
        elif a=='9':
            s.displayb()
            input("Press ENTER key to continue ")

        elif a=='10':
            ind=int(input("Enter index of node= "))
            if ind>=s.countnode():
                print("Invalid index")
            else:
                print("Data at index",ind,"=",s.singlenode(ind))
            input("Press ENTER key to continue ")

        elif a=='11':
            if s.countnode==0:
                print("Link List is Empty")
            else:
                data=int(input("Enter data of node to search ="))
                res=s.Search(data)
                if res==-1:
                    print("Node not found")
                else:
                    print("Node found at index",res)
            input("Press ENTER key to continue ")

        elif a=='12':
            print("Total number of node=",s.countnode())
            input("Press ENTER key to continue ")


        elif a=='13':
            print("*"*43)
            print(' '*16+"THANK YOU")
            print("*"*43)
            ch=False
            
        else:
            print("Invalid input")
            input("Press ENTER key to continue ")