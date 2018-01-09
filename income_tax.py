def return_income_tax(a):
    if (a <= 250000):
        print("no tax and the amount is. ",a)
    elif (a <= 500000):
        tax = a*0.05
        e_cess = a*0.02
        hs_cess = a*0.01
        total_amount = tax+e_cess+hs_cess
        final_amount = a-total_amount
        print("amount is. ",final_amount)
    elif (a <= 1000000):
        tax = a*0.2
        e_cess = a*0.02
        hs_cess = a*0.01
        total_amount = tax+e_cess+hs_cess
        final_amount = a-total_amount
        print("amount is. ",final_amount)
    elif (a > 1000000):
        tax = a*0.3
        e_cess = a*0.02
        hs_cess = a*0.01
        total_amount = tax+e_cess+hs_cess
        final_amount = a-total_amount
        print("amount is. ",final_amount)
    elif (a >= 5000000):
        tax = a*0.3
        s_tax= a*0.1
        e_cess = a*0.02
        hs_cess = a*0.01
        total_amount = tax+e_cess+hs_cess+s_tax
        final_amount = a-total_amount
        print("amount is. ",final_amount)
    else:
        tax = a*0.3
        s_tax= a*0.15
        e_cess = a*0.02
        hs_cess = a*0.01
        total_amount = tax+e_cess+hs_cess+s_tax
        final_amount = a-total_amount
        print("amount is. ",final_amount)
        
a = eval(input('enter the salary. '))
        
return_income_tax(a)
        