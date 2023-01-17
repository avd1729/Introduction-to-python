#program to check a key in dictionary
dct=eval(input("Enter a dictionary:"))
key=int(input("Enter key:"))
if key in dct:
    print("Key",key,"is present in dictionary")
else:
    print("Key",key,"is not present in dictionary")



