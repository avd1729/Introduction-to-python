#program to remove special characters from a string
char=str(input("Enter a string:"))
fin=" "
for i in char:
    if i.isalnum():
        fin+=i
    else:
        continue
print("String after removing special characters is",fin)

