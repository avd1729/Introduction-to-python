#program to display middle letters of a string
char=str(input("Enter a string having a minimum of 5 characters:"))
lgh=len(char)
fin=" "
if lgh>=5:
    lgh=lgh//2
    fin=char[lgh-1]+char[lgh]+char[lgh+1]
    print("Middle three characters of the string",fin)
else:
    print("/INVALID-12")


