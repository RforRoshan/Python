def Naive_Algorithm(txt,pat):
    pat_len=len(pat)
    txt_len=len(txt)
    l=[]
    for i in range(txt_len-pat_len+1):
        j=0
        while j<pat_len:
            if txt[i+j]!=pat[j]:
                break
            j+=1
        if j==pat_len:
            l.append(i)
    #return index
    return l


if __name__ == "__main__":

    s = "FFDFKAJKLJFSFSDFFDFFFSDOIRKFFDSLKDDFFFJAABAACAADAABAAABAAGFFDKFFFD"
    p1 = "FFD"
    p2="AABA"
    print("Pattern 1")
    a=Naive_Algorithm(s, p1)
    print("Pattern found at index ",a)
    print("Pattern 2")
    a=Naive_Algorithm(s, p2)
    print("Pattern found at index ",a)