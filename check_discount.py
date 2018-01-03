amount=int(input('Enter the price: '))
discount_percentage = input('Enter the discount percentage: ')
binding_type = str(raw_input('Enter binding type: '))


def price(amount , discount_percentage , binding_type):
    discount = 0.1*amount
    
    if(binding_type == "HB"):
        print(amount)
    else:
        discountpercent = (discount_percentage/100.00)*amount
        print(amount-discountpercent)
        
        
price(amount , discount_percentage , binding_type)