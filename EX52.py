#program to concatenate a given list which range goes from 1 to n
n=int(input("Enter limit:"))
fiv=['p','q']
fin=[]
for i in range(1,n+1):
    for j in fiv:
        fin.append(str(i)+j)
print(fin)






