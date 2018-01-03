v = raw_input("Enter a letter of the alphabet: ")
def vowels(v):
    if v in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
        print("True")
    else:
        print("False")
        
vowels(v)