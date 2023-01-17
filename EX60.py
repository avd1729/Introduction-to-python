#program to swap the first and last element of a list
lst=eval(input("Enter a list:"))
print("List before swapping:",lst)
lst[0],lst[-1]=lst[-1],lst[0]
print("List after swapping:",lst)


