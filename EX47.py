#program to find the given number in the list
lst=eval(input("Enter a list:"))
ele=int(input("Enter a element:"))
if ele in lst:
    print(ele,"is found at index",lst.index(ele))
else:
    print(ele,"is not found in list")

