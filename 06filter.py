r=[]
import random
for i in range(1,100):
    r.append(random.randint(0,100))
r2 = filter(lambda n : n//100 ==0, r)
print(list(r2))