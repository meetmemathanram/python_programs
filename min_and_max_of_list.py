import random

def ranlist(n,mn,mx):
    a=[]
    for i in range(n):
        i = random.randint(mn,mx)
        a.append(i)
    return a 

n=eval(input('Enter the range'))
mn=eval(input('min element'))
mx=eval(input('max element'))
print(ranlist(n,mn,mx))
