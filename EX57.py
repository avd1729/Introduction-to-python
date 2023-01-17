#program to find the second smallest number in a list using sorting
lst=eval(input("Enter a list:"))
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print('The second smallest number is:',lst[1])


        
