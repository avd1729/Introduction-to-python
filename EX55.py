#program to split a list based on the first letter
lst=eval(input("Enter the list of words in lowercase:"))
alph='abcdefghijklmnopqrstuvwxyz'
for i in alph:
    fin=[]
    for j in lst:
        if i==j[0]:
            c.append(j)
    if fin!=[]:
        print("The words starting with",i,"are:",)
        for x in fin:
            print(x)
            
        

    
