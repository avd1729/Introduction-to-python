#program to find the negative numbers in a list
lst=eval(input("Enter a list(/Integers only):"))
fin=[]
a=0
for i in lst:
    if i<0:
        fin.append(i)
    else:
        a+=1
print("Positive numbers in",lst,"is/are",fin)






