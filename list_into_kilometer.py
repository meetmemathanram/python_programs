def convert_list():
    km_list=[]
    a = [int(x) for x in input('Enter the value in kilometer').split()]
    for i in a:
        km_list.append(i*1.60)
    print(km_list)
    print(a)
    


convert_list()