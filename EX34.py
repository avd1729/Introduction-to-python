#program to check if a string contains any special character
char=str(input("Enter a string:"))
spl_char=[]
a=0
b=0
for i in char:
    if i.isalnum():
       a+=1 
    elif i==' ':
        b+=1
    else:
        spl_char.append(i)
print("The special characters are:",spl_char)
    
    
    
    
