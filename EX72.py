#program to remove duplicates from a dictionary
dct=eval(input("Enter a dictionary:"))
a=[]
for i in dct.copy():
    if dct[i] not in a:
        a.append(dct[i])
    else:
        dct.pop(i)
print("The modified dictionary is",dct)


    
