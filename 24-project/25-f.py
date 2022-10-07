# Creating Directory 

f=open("C:/Users/HP/Desktop/python/Assignment/24-project/file1.csv",'r')
s=f.readlines(1)
s=s[0][:-1].split(',')
#print(s)

s2=f.readlines()
s2[-1]=s2[-1]+'\n'
#print(s2)
students={}
f.close()

for i in s2:
    st=i[:-1].split(',')
    ds={}
    for j in range(0,len(s)):
        ds[s[j]]=st[j]
    students[ds[s[2]]]=ds

'''for i in students.keys():
    print(i,students[i])
'''


#Avg
for i in students.values():
    i['avg']=str((int(i['phy'])+int(i['chem'])+int(i['math'])+int(i['bio']))/4)
#print(students)


#rank
a={ float(x['avg']) for x in students.values() }
a=list(a)
a.sort(reverse=True)
#print(a)
for i in students.values():
    i['rank']=str(a.index(float(i['avg']))+1)

'''for i in students.keys():
    print(i,students[i])
print()'''


#making csv file

f=open("C:/Users/HP/Desktop/python/Assignment/24-project/file2.csv",'w')
s=students[list(students.keys())[0]]
s=','.join(s)
#print(s)
f.write(s+"\n")

for i in students.values():
    stu=list(i.values())
    stu=','.join(stu)
    f.write(stu+'\n')
f.close()
