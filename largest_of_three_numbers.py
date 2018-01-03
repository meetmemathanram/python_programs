def largest(a,b,c):
    if a>b and a>c:
        print({},'is grater'.format(a))
    elif b>c:
        print('b is grater')
    else:
        print('c is grater')

a= input('Enter the a value: ')
b= input('Enter the b value: ')
c= input('Enter the c value: ')

largest(a, b, c)