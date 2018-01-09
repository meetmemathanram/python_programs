import random

def ranlist(n):
    a=[]
    for i in range(n):
        i = random.randint(50,100)
        a.append(i)
    return a

n=int(input('Enter the range'))
print(ranlist(n))
