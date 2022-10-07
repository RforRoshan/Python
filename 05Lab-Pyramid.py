n=int(input("Enter No. of lines: "))
c=input("Enter a Character: ")
for i in range(1,n+1):
    print((n-i)*" "+(2*i-1)*c)
for i in range(1,n):
    print((i)*" "+(2*n-1-2*i)*c)