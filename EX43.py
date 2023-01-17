#program to identify strings with both alphabets and numbers
char=str(input("Enter a string:"))
fin=char.split()
a=0
for i in fin:
    if(i.isalpha()==False and i.isdigit()==False and i.isalnum()==True):
        print("The string contains both alphabets and numbers")
        a+=1
if a==0:
    print("The string doesn't contain both alphabets and numbers")

