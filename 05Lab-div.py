a=int(input("Enter the Starting range: "))
b=int(input("Enter the Ending range: "))
c=int(input("Enter the Divisor: "))
for i in range(a,b+1):
    if i%c==0:
        print(i,end=" ")