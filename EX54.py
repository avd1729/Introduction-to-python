#program to convert a list of multiple integers into a string
lst=eval(input("Enter a list(/integers):"))
fin=''
for i in lst:
    fin=fin+''+str(i)
print(fin)


