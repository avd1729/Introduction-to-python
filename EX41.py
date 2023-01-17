#Program to count the highest occurring substrings
char=str(input("Enter the #main_string:"))
sub_char=str(input("Enter substring to be found in the #main_string:"))
count=char.count(sub_char)
if count!=0:
    print("The count of",sub_char,"in",char,"is",count)
else:
    print("The substring",sub_char,"is not found in",char)
