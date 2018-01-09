#1. Write a function to find the selling price of the book when the list price
#and discount_percentage are given given. 
#Discount percentage should be optional. 
#When no value is provided, 
#the function will assume that the value is 10%
def getsellingprice(list_price , discount_percentage = 0.1):
    sellingprice = list_price*discount_percentage 
    discount = list_price-sellingprice
    print(discount)
        
list_price= int(input('Enter the list price'))
getsellingprice(list_price)
                #enter the value optional)