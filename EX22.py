#program to get n numbers and display it in ascending order
lst=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    block=input("Enter the elements:")
    lst.append(block)
print("Original list is:",lst)
for i in range(n):
    for j in range(0,n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print("The elements in ascending order",lst)
