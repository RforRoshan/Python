def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


d=bubbleSort(['zebra', 'goat', 'ant', 'elephant', 'buffalo'])
e=bubbleSort([5,6,55,66,1])
print(d,e)