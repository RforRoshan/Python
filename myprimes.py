def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True


def getprimes(start, end):
    s=""
    for i in range(start,end+1):
        if (checkprime(i)==True):
            s=s+str(i)+" "
    return s


def gethighestprime(n):
    for i in range(n,1,-1):
        if (checkprime(i)==True):
            return i

#print("myprimes.py __name__ = ", __name__)

if __name__ == '__main__':
    # input
    n = int(input("Enter a number: "))

    # process/output
    if(checkprime(n) == True):
        print('The number is prime')
    else:
        print('The number is not prime')