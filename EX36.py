#program to count the different characters in a string
char=str(input("Enter a string:"))
ch=len(char)
alph=0
dig=0
spc=0
syb=0
for i in char:
    if i.isalpha():
        alph+=1
    elif i.isdigit():
        dig+=1
    elif i.isspace():
        spc+=1
    else:
        syb+=1
print("Total characters:",ch)
print("Alphabets:",alph)
print("Digits:",dig)
print("Space:",spc)
print("Symbols:",syb)    
