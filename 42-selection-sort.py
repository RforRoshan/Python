def selection_sort(l,asc=True):
    if asc==True:
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):
                if l[i]>l[j]:
                    temp=l[j]
                    l[j]=l[i]
                    l[i]=temp
        return l
    else:
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):
                if l[i]<l[j]:
                    temp=l[j]
                    l[j]=l[i]
                    l[i]=temp
        return l



def selection_sort_mix(l,asc=True):
    l=list(map(str,l))
    if asc==True:
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):
                if l[i]>l[j]:
                    temp=l[j]
                    l[j]=l[i]
                    l[i]=temp
        return l
    else:
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):
                if l[i]<l[j]:
                    temp=l[j]
                    l[j]=l[i]
                    l[i]=temp
        return l



if __name__ == '__main__':
    print(selection_sort([9, 1, 3, 5, 7, 8, 2, 4, 6, 6, 6]))  # 1, 2, 3, 4
    print(selection_sort([4, 1, 3, 2])) # 4, 3, 2, 1
    print(selection_sort([4, 1, 3, 2], asc=False))


    print(selection_sort_mix([3, 4, 5, 1.3,  'zebra', 'goat', 'ant', 'elephant', 'buffalo', -67, 78]))