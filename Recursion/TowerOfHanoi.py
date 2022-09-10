def TowerOfHanoi(n , a, c, b):
    if n == 0:
        return
    TowerOfHanoi(n-1, a, b, c)
    print("Move disk",n,"from rod",a,"to rod",c)
    TowerOfHanoi(n-1, b, c, a)

n=int(input("Enter no. of disk = "))
TowerOfHanoi(n, 'A', 'C', 'B') 