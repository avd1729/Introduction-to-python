#program to find the second largest number in a list
lst=eval(input("Enter a list:"))
lgh=len(lst)
lst.sort()
sec=lst[lgh-2]
print("Second smallest element is:",sec)


