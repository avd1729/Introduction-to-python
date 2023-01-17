#program to capitalize the first and last character of a string
char=str(input("Enter a tring:"))
char=char[0].upper()+char[1:len(char)-1]+char[-1].upper()
print(char)

