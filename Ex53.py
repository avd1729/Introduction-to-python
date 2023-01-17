#program to find common elements from two lists
lst1=eval(input("Enter first list:"))
lst2=eval(input("Enter second list:"))
fin=[]
for i in lst1:
    for j in lst2:
        if i==j:
            fin.append(i)
print("Common elements:",fin)



            
