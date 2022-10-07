class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binary_Tree:
    def __init__(self):
        self.root=None
  
    def create(self):
        def create_tree(root):
            a=int(input("Enter data = "))
            new_node=node(a)
            print("*"*43)
            print("CHOICE  OPERATION")
            print("  1     Insert child node of",a)
            print("  0     No child node")
            print("*"*43)
            b=input("Enter your choice= ")
            if b=="1":
                print("Insert node left of",a)
                new_node.left=create_tree(root)
                print("Insert node right of",a)
                new_node.right=create_tree(root)
            return new_node

        root=self.root
        self.root=create_tree(root)
        print("*"*43)
        print("Tree created")
        print("*"*43)

    def Preorder(self):
        root=self.root
        def dis(root):
            if root:
                print(root.data,end="  ")
                dis(root.left)
                dis(root.right)
        print("-----Preorder Traversals------")
        dis(root)
        print()

    def Inorder(self):
        root=self.root
        def dis(root):
            if root:
                dis(root.left)
                print(root.data,end="  ")
                dis(root.right)
        print("-----Inorder Traversals------")
        dis(root)
        print()

    def Postorder(self):
        root=self.root
        def dis(root):
            if root:
                dis(root.left)
                dis(root.right)
                print(root.data,end="  ")
        print("-----Postorder Traversals------")
        dis(root)
        print()

        
if __name__=="__main__":
    s=Binary_Tree()
    ch=True
    while(ch):
        print("*"*43)
        print("CHOICE  BINARY TREE OPERATION")
        print("  1     Create New Tree")
        print("  2     Preorder traversal")
        print("  3     Inorder traversal")
        print("  4     Postorder traversal")
        print("  5     Exit")
        print("*"*43)
        a=input("Enter your choice= ")
        if a=="1":
            s.create()
            input("Press ENTER key to continue ")
        elif a=="2":
            s.Preorder()
            input("Press ENTER key to continue ")
        elif a=="3":
            s.Inorder()
            input("Press ENTER key to continue ")
        elif a=="4":
            s.Postorder()
            input("Press ENTER key to continue ")
        elif a=='5':
            print("*"*43)
            print(' '*16+"THANK YOU")
            print("*"*43)
            ch=False       
        else:
            print("Invalid input")
            input("Press ENTER key to continue ")