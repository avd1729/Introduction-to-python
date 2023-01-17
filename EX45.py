#program to check the given list elements are in ascending order
lst=list(input("Enter a list:"))
lstt=lst.sort()
if lst == lstt:
    print("Given list elements are in ascending order")
else:
    print("Given list elements are not in ascending order")

    
