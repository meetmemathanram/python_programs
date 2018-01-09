def ranlist(n):
    a=[]
    for x in range(n):
        a.append(x*2)
    return a 

n=eval(input('Enter the range'))
#mn=eval(input('min element'))
#mx=eval(input('max element'))
print(ranlist(n))