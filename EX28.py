#program to compute the diagonal of a matrix
lst=[]
x=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(x)):
    for j in range(len(x[i])):
        if i==j:
            lst.append(x[i][j])
print(lst)
