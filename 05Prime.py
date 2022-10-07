a=int(input("Enter a number: "))
p=True
for i in range(2,a):
    if(a%i==0):
        p=False
if p==True:
    print("No. is Prime")
