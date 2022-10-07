
def genReport(dd):
    dottedline = '-'*70
    template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:3}'
    
    print('CLASS REPORT')
    print(dottedline)
    print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
    print(dottedline)
    for regid in dd.keys():
        name = dd[regid]['name']
        age  = dd[regid]['age']
        regid = dd[regid]['regid']
        phy = dd[regid]['phy']
        chem = dd[regid]['chem']
        math = dd[regid]['math']
        bio = dd[regid]['bio']
        avg = dd[regid]['avg']
        rank = dd[regid]['rank']
        print(template.format( regid, name, age,phy, chem, math, bio, avg, rank))
    print(dottedline)

# [LAB] Complete the function definition
# It should write the report to the file specified by "path"
def write2file(dd, path):
    f=open(path,'w')
    dottedline = '-'*70
    template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:3}'
    f.write('CLASS REPORT\n')
    f.write(dottedline+'\n')
    f.write(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
    f.write('\n'+dottedline+'\n')
    #sorting rank 
    ranklist=[int(a['rank']) for a in dd.values()]
    ranklist.sort()
    for i in range(0,len(ranklist)):
        for regid in dd.keys():
            if ranklist[i]==(int(dd[regid]['rank'])):
                name = dd[regid]['name']
                age  = dd[regid]['age']
                regid = dd[regid]['regid']
                phy = dd[regid]['phy']
                chem = dd[regid]['chem']
                math = dd[regid]['math']
                bio = dd[regid]['bio']
                avg = dd[regid]['avg']
                rank = dd[regid]['rank']
                f.write(template.format( regid, name, age,phy, chem, math, bio, avg, rank))
                f.write('\n')
    f.write(dottedline)
    f.close()

# Read the csv file as a text file
f=open("C:/Users/HP/Desktop/python/Assignment/24-project/file1.csv",'r')
content=f.read()
f.close()
print(content)
print('-'*60 + ' > First Step')



# ------------------------ csv file is read and its content is available for further processing

# Read the coloums --> name,age,regid,phy,chem,math,bio,avg,rank
# Read a row --> Vijay,14,HPE001,99,98,97,96,0,0
# Construct a dictionary out of the column and the row
# Add that dictionary to the main dictionry that represents the class
# Repeat this process for all the entries in the csv file

f=open("C:/Users/HP/Desktop/python/Assignment/26/file1.csv",'r')
s=f.readlines(1)
s=s[0][:-1].split(',')
#print(s)

s2=f.readlines()
s2[-1]=s2[-1]+'\n'
#print(s2)
classdict={}
f.close()

for i in s2:
    st=i[:-1].split(',')
    ds={}
    for j in range(0,len(s)):
        ds[s[j]]=st[j]
    classdict[ds[s[2]]]=ds

print(classdict)
print('-'*60 + ' > Second Step')

# ------------------------- csv data is in the form of a dictionary

# Access the dictionary iteratively and calculate the average marks and
# update in the dictionary

# [LAB] Write code to calculate the average for all the students
for i in classdict.values():
    i['avg']=str((int(i['phy'])+int(i['chem'])+int(i['math'])+int(i['bio']))/4)

print(classdict)
print('-'*60 + ' > Third Step')

# ------------------------- dictionary updated with average data

# Calculate the rank
# collect all the averages -> into a list
# arrange the averages in descending order
# iterate the entire dictionary and update the rank based on the descending
# order of averages

# [LAB] Write code to calculate the rank for all the students
a={ float(x['avg']) for x in classdict.values() }
a=list(a)
a.sort(reverse=True)
#print(a)
for i in classdict.values():
    i['rank']=str(a.index(float(i['avg']))+1)
print(classdict)
print('-'*60 + ' > Fourth Step')   



# ------------------------- dictionary updated with rank data

# Re-write the csv file

path = r"C:/Users/HP/Desktop/python/Assignment/26/students_completed.csv"

f=open(path,'w')
s=classdict[list(classdict.keys())[0]]
s=','.join(s)
#print(s)
f.write(s+"\n")

for i in classdict.values():
    stu=list(i.values())
    stu=','.join(stu)
    f.write(stu+'\n')
f.close()

# ------------------------- resultant csv file is now ready with averages and ranks updated

genReport(classdict)
write2file(classdict, r"C:/Users/HP/Desktop/python/Assignment/26/report2.txt")