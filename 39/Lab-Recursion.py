def rec(n):
    if n<0:
        print("Zero!")
        return 0
    print(n,'\U0001F606'*(n))
    return rec(n-2)

rec(9)