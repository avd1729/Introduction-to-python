#program to check if given string is palindrome or not
char=str(input("Enter a string:"))
lst1=char[0:]
lst2=char[::-1]
if lst1==lst2:
    print(char,"is a palindrome.")
else:
    print(char,"is not palindrome.")
    
