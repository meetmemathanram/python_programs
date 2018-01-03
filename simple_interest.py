'''
Created on 02-Jan-2018

@author: mathan
'''
p = input('Enter the principal. ')
n = input('Enter the number of years. ')
r = input('Enter the rate of interest in percentage. ')

def si(p,n,r):
    simple_interest = p*n*r/100
    total_amount = p+simple_interest
    print("simple interest is: %d"%simple_interest)
    print("Total amount is: %d"%total_amount)

 
si(p,n,r)