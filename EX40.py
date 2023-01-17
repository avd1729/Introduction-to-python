#program to to find a word made with the 1st, middle and last letters of the given word.
char=str(input("Enter a string with a minimum of three characters:"))
fin=" "
lgh=len(char)
f=char[0]
m=char[lgh//2]
l=char[-1]
fin+=f+m+l
print("String is:",fin)
