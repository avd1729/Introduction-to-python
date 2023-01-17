#program to replace the special characters in a string with '#'
char=str(input("Enter a string:"))
fin=" "
for i in char:
    if i.isalnum():
        fin+=i
    else:
        fin+="#"
print("String after replacement:",fin)
