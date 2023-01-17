#program to find all occurences of a substring within a string
char=str(input("Enter a string:"))
sub_char=[]
for i in char:
    sub_char.append(i)
sub_char=set(sub_char)
for i in sub_char:
    print("The count of",i,"is:",char.count(i))
