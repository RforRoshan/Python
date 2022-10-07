def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        merge_sort(L)
        R=arr[mid:]
        merge_sort(R)
        n1=len(L)
        n2=len(R)


        i=j=k=0
        while(i<n1 and j<n2):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        
        while(i<n1):
            arr[k]=L[i]
            i+=1
            k+=1
        
        while(j<n2):
            arr[k]=R[j]
            j+=1
            k+=1


if __name__=="__main__":
    arr=[5,4,6,8,9,7,2,1]
    merge_sort(arr)
    print(arr)